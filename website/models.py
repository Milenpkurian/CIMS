from . import dep

# %!@!@#%@!$%@!%&^@#%!@$^@!$#%$!@%#%%$!@#%$!@#!^_____________DEPARTMENT DATABASE____________________ %!@!@#%@!$%@!%&^@#%!@$^@!$#%$!@%#%%$!@#%$!@#!^

# __________________________LAB________________________________________

#Creating model table for our CHEMICALS in dep database
class Chemicals(dep.Model):
    id = dep.Column(dep.String(100), primary_key = True)
    item_name = dep.Column(dep.String(100))
    item_type = dep.Column(dep.String(100))
    in_stock = dep.Column(dep.String(100))
    received_date=dep.Column(dep.Date())
    expiry_date=dep.Column(dep.Date())

    def __init__(self,id, item_name, item_type , in_stock,received_date,expiry_date):
 
        self.id = id
        self.item_name = item_name
        self.item_type = item_type
        self.in_stock=in_stock
        self.received_date=received_date
        self.expiry_date=expiry_date


#glasswares
class Glasswares(dep.Model):
    id = dep.Column(dep.String(100),primary_key=True)
    item_name=dep.Column(dep.String(100))
    quantity=dep.Column( dep.Integer )
    defective=dep.Column( dep.Integer )

    def __init__(self,id,item_name,quantity,defective):
        self.id=id
        self.item_name=item_name
        self.quantity=quantity
        self.defective=defective


#Equipments
class Equipments(dep.Model):
    id = dep.Column(dep.String(100),primary_key=True)
    item_name=dep.Column(dep.String(100))
    quantity=dep.Column( dep.Integer )
    defective=dep.Column( dep.Integer )

    def __init__(self,id,item_name,quantity,defective):
        self.id=id
        self.item_name=item_name
        self.quantity=quantity
        self.defective=defective


#____________________________   Request from Lab to Hod____________________
class Req_lab(dep.Model):
    id = dep.Column(dep.String(100), primary_key = True)
    item_name = dep.Column(dep.String(100))
    item_type = dep.Column(dep.String(100))
    req_qty = dep.Column(dep.String(100))
    need_for=dep.Column(dep.String(500))
    status=dep.Column(dep.String(100))

    def __init__(self,id, item_name, item_type , req_qty,need_for,status ):
 
        self.id = id
        self.item_name = item_name
        self.item_type = item_type
        self.req_qty=req_qty
        self.need_for=need_for
        self.status=status







#_____________________________                HOD                  ____________________________________

#Furniture
class Furniture(dep.Model):
    id = dep.Column(dep.String(100),primary_key=True)
    item_name=dep.Column(dep.String(100))
    quantity=dep.Column( dep.Integer )
    defective=dep.Column( dep.Integer )

    def __init__(self,id,item_name,quantity,defective):
        self.id=id
        self.item_name=item_name
        self.quantity=quantity
        self.defective=defective

#Electronics
class Electronics(dep.Model):
    id = dep.Column(dep.String(100),primary_key=True)
    item_name=dep.Column(dep.String(100))
    quantity=dep.Column( dep.Integer )
    defective=dep.Column( dep.Integer )

    def __init__(self,id,item_name,quantity,defective):
        self.id=id
        self.item_name=item_name
        self.quantity=quantity
        self.defective=defective

#Computers
class Computers(dep.Model):
    id = dep.Column(dep.String(100),primary_key=True)
    item_name=dep.Column(dep.String(100))
    quantity=dep.Column( dep.Integer )
    defective=dep.Column( dep.Integer )

    def __init__(self,id,item_name,quantity,defective):
        self.id=id
        self.item_name=item_name
        self.quantity=quantity
        self.defective=defective

