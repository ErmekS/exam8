from django.contrib.auth import get_user_model
from django.db import models
# from django.urls import reverse

# Create your models here.


CATEGORY_CHOICES = [('Confectionery', 'Кондитерка'), ('Grocery', 'Бакалея'), ('Drinks', 'Напитки')]
GRADE_CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Product(BaseModel):
    product_name = models.CharField(max_length=35, null=False, blank=False, verbose_name="Название продукта")
    category = models.CharField(max_length=20, null=False, blank=False, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name="Категория продукта")
    product_description = models.TextField(max_length=3000, verbose_name="Описание продукта")
    product_img = models.ImageField(upload_to="product_img", null=True, blank=True, verbose_name="Фото продукта")

    def __str__(self):
        return f"{self.id}. {self.product_name}."

    # def get_absolute_url(self):
    #     return reverse("webapp:ProductView", kwargs={"pk": self.pk})

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Review(BaseModel):
    author = models.ForeignKey(get_user_model(), related_name="reviews", verbose_name="Автор", default=1,
                               on_delete=models.SET_DEFAULT)
    product = models.ForeignKey("webapp.Product", on_delete=models.CASCADE, related_name="products",
                                verbose_name="Продукт")
    feedback_text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Текст отзыва к продукту")
    grade = models.CharField(max_length=20, null=False, blank=False, choices=GRADE_CHOICES, default=GRADE_CHOICES[0][0],
                             verbose_name="Оценка продукта")
    feedback_moderated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}. {self.author}"

    class Meta:
        db_table = "review"
        verbose_name = "отзыв"
        verbose_name_plural = "Список отзывов"
