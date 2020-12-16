class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        print(f'    {self.name} - {self.duration} мин.')

class Album:
    def __init__(self, album_name, group):
        self.name = album_name
        self.group = group
        self.tracks = []

    def get_tracks(self):
        print(f'Альбом: {self.name} Группа: {self.group}')
        for track in self.tracks:
            track.__str__()

    def add_track(self, name, duration):
        self.tracks.append(Track(name, duration))

    def get_duration(self):
        duration = 0
        for track in self.tracks:
            duration += track.duration
        return duration

def collection():
    album_1 = Album('Группа крови', "Кино")
    album_2 = Album('Черный альбом', "Кино")
    album_1.add_track('Группа крови', 4)
    album_1.add_track('Закрой за мной дверь, я ухожу', 4)
    album_1.add_track('Война', 4)
    album_2.add_track('Кончится лето', 5)
    album_2.add_track('Звезда', 4)
    album_2.add_track('Кукушка', 6)
    album_1.get_tracks()
    album_2.get_tracks()
    return album_1, album_2
alb_1, alb_2 = collection()
print(f'Длительность 1 альбома: {alb_1.get_duration()} мин')
print(f'Длительность 2 альбома: {alb_2.get_duration()} мин')