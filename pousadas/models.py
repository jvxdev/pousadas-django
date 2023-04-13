from django.db import models

class Pousada(models.Model):
    QTD_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("Mais de 5", "Mais de 5")
    )

    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    cep = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    quartos = models.CharField(max_length=10, choices=QTD_CHOICES, blank=False, null=False)
    banheiros = models.CharField(max_length=10, choices=QTD_CHOICES, blank=False, null=False)
    imagem = models.ImageField(null=True, blank=True, upload_to="images/")

REQUIRED_FIELDS = '__all__'