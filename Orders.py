class Order(models.Model):
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)