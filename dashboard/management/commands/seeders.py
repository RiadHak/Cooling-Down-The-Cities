import random
from dashboard.models import Seeders
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        for _ in range(100):
            temp = random.uniform(-20, 50)
            co2 = random.uniform(300, 5000)
            Luchtdruk = random.uniform(940, 1060)
            Luchtvochtigheid = random.uniform(0, 100)
            Luchtkwaliteit = random.uniform(1, 5)
            Seeders.objects.create(
                temperatuur = temp,
                CO2 = co2,
                luchtvochtigheid = Luchtvochtigheid,
                luchtdruk = Luchtdruk,
                luchtkwaliteit = Luchtkwaliteit
            )
        self.stdout.write(
            self.style.SUCCESS('100 random metingen gecreëerd')
        )
            
        
        
    