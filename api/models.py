from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class ArtCategory(models.TextChoices):
    PAINTING = 'УРАН ЗУРАГ', 'Уран зураг'
    SCULPTURE = 'УРАН БАРИМАЛ', 'Уран баримал'
    PHOTOGRAPHY = 'ФОТО ЗУРАГ', 'Фото зураг'
    DIGITAL = 'ДИЖИТАЛ УРАН БҮТЭЭЛ', 'Дижитал уран бүтээл'
    MIXED = 'ХОЛИМОГ БҮТЭЭЛ', 'Холимог уран бүтээл'
    OTHER = 'БУСАД', 'Бусад'
    
class ArtTechnique(models.TextChoices):
    OIL = 'ЗОТОН ТОС', 'Зотон тос'
    ACRYLIC = 'ЗОТОН АКРИЛИК', 'Зотон акрилик'
    WATERCOLOR = 'УСАН БУДАГ ЦААС', 'Усан будаг цаас'
    PENCIL = 'ХАРАНДААН ТЕХНИК', 'Харандаа'
    DIGITAL = 'ДИЖИТАЛ ТЕХНИК', 'Дижитал техник'
    MIXED = 'ХОЛИМОГ ТЕХНИК', 'Холимог техник'
    OTHER = 'БУСАД ТЕХНИК', 'Бусад техник'
    
class Artist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    profile = models.ImageField(upload_to='artists/', null=True, blank=True)
    contact = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=f'products/', null=False, blank=False)
    artist = models.ForeignKey(
        Artist, 
        on_delete=models.CASCADE, 
        related_name='products'
    )
    price = models.DecimalField(
        max_digits=15, 
        decimal_places=0, 
        validators=[MinValueValidator(0)]
    )
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    category = models.CharField(
        max_length=20,
        choices=ArtCategory.choices,
        default=ArtCategory.PAINTING
    )
    technique = models.CharField(
        max_length=20,
        choices=ArtTechnique.choices,
        default=ArtTechnique.ACRYLIC
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.title} by {self.artist.name}"
    
    class Meta:
        ordering = ['-created_at']