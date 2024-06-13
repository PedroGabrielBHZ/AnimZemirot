# ========================================================
# Songs Model
#
# Example scheme:
# [
#     {
#         "id": 1,
#         "nameTransliterated": "Achat sha'alti",
#         "nameHebrew": "אחת שאלתי",
#         "nameEnglish": "One thing I ask",
#         "lyricsTransliterated": "Achat sha'alti me'eit Hashem, otah avakesh:\n shivti b'veit Hashem, kol y'mei chayai, lachazot\n b'noam Hashem, u'l'vaker b'heikhalo.",
#         "lyricsHebrew": "אַחַת שָׁאַלְתִּי מֵאֵת-יְהוָה אוֹתָהּ אֲבַקֵּשׁ:\n שִׁבְתִּי בְּבֵית-יְהוָה, כָּל-יְמֵי חַיַּי,\n לַחֲזוֹת בְּנֹעַם-יְהוָה, וּלְבַקֵּר בְּהֵיכָלוֹ.",
#         "lyricsEnglish": "One thing I ask from the Lord, one thing I desire\n That I might dwell in Your house all the days of my life \n To behold the graciousn​ess of the Lord, and to enter God's sanctuary​."
#     }
# ]
# ========================================================
import json


PAGE_SIZE = 100


class Song:
    """
    Represents a song object.

    Attributes:
        id (int): The unique identifier of the song.
        nameTransliterated (str): The transliterated name of the song.
        nameHebrew (str): The Hebrew name of the song.
        nameEnglish (str): The English name of the song.
        lyricsTransliterated (str): The transliterated lyrics of the song.
        lyricsHebrew (str): The Hebrew lyrics of the song.
        lyricsEnglish (str): The English lyrics of the song.
    """

    # mock songs database
    db = {}

    def __init__(
        self,
        id,
        nameTransliterated,
        nameHebrew,
        nameEnglish,
        lyricsTransliterated,
        lyricsHebrew,
        lyricsEnglish,
    ):
        self.id = id
        self.nameTransliterated = nameTransliterated
        self.nameHebrew = nameHebrew
        self.nameEnglish = nameEnglish
        self.lyricsTransliterated = lyricsTransliterated
        self.lyricsHebrew = lyricsHebrew
        self.lyricsEnglish = lyricsEnglish

    def __str__(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False)

    def update(self, **kwargs):
        """
        Updates the song object with the provided key-value pairs.

        Args:
            **kwargs: Key-value pairs representing the attributes to be updated.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def all(cls, page=1):
        """
        Retrieves a list of songs.

        Args:
            page (int): The page number to retrieve. Default is 1.

        Returns:
            list: A list of song objects.
        """
        page = int(page)
        start = (page - 1) * PAGE_SIZE
        end = start + PAGE_SIZE
        return list(cls.db.values())[start:end]

    @classmethod
    def search(cls, query):
        """
        Searches for songs by name or lyrics.

        Args:
            query (str): The search query.

        Returns:
            list: A list of song objects that match the search query.
        """
        query = query.lower()
        return [
            song
            for song in cls.db.values()
            if query in song.nameTransliterated.lower()
            or query in song.nameHebrew.lower()
            or query in song.nameEnglish.lower()
            or query in song.lyricsTransliterated.lower()
            or query in song.lyricsHebrew.lower()
            or query in song.lyricsEnglish.lower()
        ]

    @classmethod
    def load_db(cls):
        """
        Loads the songs database from a JSON file.
        """
        with open("songs.json", "r", encoding="utf-8") as file:
            songs = json.load(file)
            for song in songs:
                cls.db[song["id"]] = Song(**song)
