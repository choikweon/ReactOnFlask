import json
import requests
from flask_babel import _

def translate(text, source_language, dest_language):
    print("[DeBuG] source : " + source_language + " dest : " + dest_language) 
    if(dest_language=='ko'):
        return "이 글은 번역되었습니다. 진짜로."
    else:
        return "not really translated into " + dest_language + " : " + text