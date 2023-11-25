
class Customers:
    customer_id = ""
    step_seconds = 0
    picking_offset = 0

    def __init__(self, customer_id, step_seconds=0, picking_offset=0):
        self.customer_id = customer_id
        self.step_seconds = step_seconds
        self.picking_offset = picking_offset

    def __eq__(self, other):
        if not isinstance(other, Customers):
            raise Exception("Can't compare to another class type")
        return self.customer_id == other.customer_id