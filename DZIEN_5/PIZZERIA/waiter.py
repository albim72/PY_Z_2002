class Waiter:
    def __init__(self):
        self.builder = None
        
    def construct_pizza(self,builder):
        self.builder = builder
        steps = (builder.prepare_dough,
                 builder.add_souce,
                 builder.add_topping,
                 builder.bake)
        [step() for step in steps]
        
    @property
    def pizza(self):
        return self.builder.pizza
