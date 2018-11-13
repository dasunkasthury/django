from django.db import models

class album(models.Model):
    artist =models.CharField(max_length =250)
    album_title = models.CharField(max_length =250)
    genre =models.CharField(max_length =250)
    album_logo = models.CharField(max_length =1000)


    def __str__ (self):
        return self.album_title + '_' + self.artist



class song(models.Model):
    album =models.ForeignKey(album, on_delete =models.CASCADE)
    file_type = models.CharField(max_length =250)
    song_title =models.CharField(max_length =250)
