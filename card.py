from PIL import Image, ImageDraw, ImageFont
import textwrap

TITLE_FONT_SIZE = 35
RULES_FONT_SIZE = 18
NO_SPACES_IN_IMG_FILES = False # Cockatrice requires file names to match card name exactly by default, including spaces.
                               # Can be set to true if including custom card xml

titleF = ImageFont.truetype('fonts/roboto/Roboto-Black.ttf', TITLE_FONT_SIZE)
rulesF = ImageFont.truetype('fonts/source-code-pro/SourceCodePro-Medium.otf', RULES_FONT_SIZE)

def filize(fileName, extension):
    if NO_SPACES_IN_IMG_FILES or extension != 'png':
        fileName = fileName.replace(' ', '_')
    return f"{fileName}.{extension}"

def makeCardImage(name, rules):
    img = Image.new('RGB', (500, 726), color = 'white')

    rulesf = textwrap.fill(rules, 40) #wrap that text bb

    d = ImageDraw.Draw(img)
    d.text((20,20), name, fill=(0,0,0), font=titleF)
    d.text((20,500), rulesf, fill=(0,0,0), font=rulesF)

    file = filize(name, 'png')
    img.save(file)

    return file

class Card:
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules
        self.image = makeCardImage(name, rules)
