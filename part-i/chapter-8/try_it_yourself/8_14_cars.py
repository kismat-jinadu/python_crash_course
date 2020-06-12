def make_car(manufacturer, model_name,**car_info):
    """build dictionary with info about a car"""
    car_info['manufacturer']=manufacturer
    car_info['model_name']=model_name
    return car_info

car_description=make_car('renault','megane',
                colour='blue', year=2010,reverse_cam =True)
print(car_description)