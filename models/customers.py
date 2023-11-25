
class Customers:
    customer_id = ""
    step_seconds = 0
    picking_offset = 0

    def __init__(self, customer_id, step_seconds, picking_offset):
        self.customer_id = customer_id
        self.step_seconds = step_seconds
        self.picking_offset = picking_offset