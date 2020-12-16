class Track:

    def __init__(self, track_name, duration):
        self.track_name = track_name
        self.duration = int(duration)

    def __str__(self):
        return f'{self.track_name} - {self.duration}'

    def __gt__(self, contrast):
        if not isinstance(contrast, Track):
            return
        return self.duration > contrast.duration

class Album:
    album_name = ''
    group = ''
    track_list = []

    def __str__(self):
        return f'Альбом - {self.album_name} : Группа -{self.group}\n' + self.get_tracks()

    def get_tracks(self):
        lists = ''
        for track in self.track_list:
            if isinstance(track, Track):
               lists = lists + str(track) + '\n'
        return lists

    def add_track(self, new_track):
        self.track_list.append(new_track)

    def get_duration(self):
        duration = 0
        for track in self.track_list:
            duration += track.duration
        return duration

album_1 = Album()
album_1.album_name = 'Группа крови'
album_1.group = 'Кино'
album_1.track_list = [Track('Группа крови', 4),
                      Track('Закрой за мной дверь, я ухожу', 4),
                      Track('Война', 4)]

album_2 = Album()
album_2.album_name = 'Черный альбом'
album_2.group = 'Кино'
album_2.track_list = [Track('Кончится лето', 5),
                      Track('Звезда', 4),
                      Track('Кукушка', 6)]

def all_albums_duration(albums_list):
    for album in albums_list:
        print(f'Альбом {album.name} длится: {album.get_duration()} мин.')
print(album_1)
print(album_2)

print("Сравнение треков:")
track1 = Track('Кончится лето', 5)
track2 = Track('Кукушка', 6)
print(track1)
print(track2)
print(track1 > track2)