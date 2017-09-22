import json

with open("sample_diction.json", "r") as f: # open(fname, mode)
    f_string = f.read()  # a str
    response_diction = json.loads(f_string)
    photo_dictionary = response_diction["photo"]


class Photo(object):
    def __init__(self, photo_dict):
        self.owner = {
            'username': photo_dict['owner']['username'],
            'realname': photo_dict['owner']['realname'],
            'location': photo_dict['owner']['location']
            }
        self.title = photo_dict['title']['_content']
        self.tags = []
        for tag in photo_dict["tags"]['tag']:
            self.tags.append(tag["raw"])
        self.media = photo_dict["media"]
        self.date_taken = photo_dict["dates"]["taken"]
        self.description = photo_dict['description']['_content']
        self.id = photo_dict['id']
        self.url = []
        for url in photo_dict['urls']['url']:
            self.url.append(url['_content'])
        self.licence = photo_dict['license']

    def __str__(self):
        return self.title

    def __repr__(self):
        return 'ID: {1}, Title: {0}, URL: {2}'.format(self.title, self.id,
        self.url)

    def __contains__(self, test_string):
            # if 'Nature' in test_string:
            #     print("This is a photo taged as Nature!")
        return(
            test_string in self.tags
            or test_string in self.title
            )

    # def __str__(self):
    #     return "{} (real name: {}) uploaded the media titled {}." \
    #     " This {} was taken on {} and is taged with {}".format(
    #                                     self.owner['username'],
    #                                     self.owner['realname'],
    #                                     self.title,
    #                                     self.media,
    #                                     self.date_taken,
    #                                     self.tags)

photo = Photo(photo_dictionary)
print(photo)
print(photo.__repr__())
