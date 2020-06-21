import xml.etree.ElementTree as ET

def search():
    """
    This function responds to a request for /api/categories
    with the complete lists of loot categories

    :return:        sorted list of categories
    """
    from xml.dom import minidom
    mydoc = minidom.parse('./dayzOffline.chernarusplus/cfglimitsdefinition.xml')
    items = mydoc.getElementsByTagName('category')
    return [item.attributes['name'].value for item in sorted(items, key=lambda x: x.attributes['name'].value)]

def post(value):
    """
    This function responds to a post for /api/categories?name=string
    with a success or failure messagte

    :return:        sucess or failure message
    """

    if value.lower() in search():
        return 'Server Error', 500, {'x-error': 'category already exists'}

    import xml.etree.ElementTree as ET
    tree = ET.parse('./dayzOffline.chernarusplus/cfglimitsdefinition.xml')
    root = tree.getroot()
    categories = root.find('categories')
    element = categories.makeelement('category', {'name':value.lower()})
    categories.append(element)
    tree.write('./dayzOffline.chernarusplus/cfglimitsdefinition.xml')
    return 'Success', 200

def delete(value):
    """
    This function responds to a delete for /api/categories/{value}
    with a success or failure messagte

    :return:        sucess or failure message
    """

    # TODO: Remove all usages of category in other files

    if not value.lower() in search():
        return 'Not Found', 404, {'x-error': 'category does not exist'}

    tree = ET.parse('./dayzOffline.chernarusplus/cfglimitsdefinition.xml')
    root = tree.getroot()
    categories = root.find('categories')
    for elem in categories.findall(f'.//category[@name="{value.lower()}"]'):
        categories.remove(elem)         
    tree.write('./dayzOffline.chernarusplus/cfglimitsdefinition.xml')
    return 'Success', 200