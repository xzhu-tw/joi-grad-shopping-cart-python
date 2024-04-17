class Order:
    def __init__(self, loyalty_points_earned, total_before_discount, total_discount, total_after_discount):
        self.loyalty_points_earned = loyalty_points_earned
        self.total_before_discount = total_before_discount
        self.total_discount = total_discount
        self.total_after_discount = total_after_discount

    def __str__(self):
        return (f"Original Total: ${self.total_before_discount:.2f}\n"
                f"Total Discount: ${self.total_discount:.2f}\n"
                f"Final Total: ${self.total_after_discount:.2f}\n"
                f"Loyalty Points Earned: {self.loyalty_points_earned}")