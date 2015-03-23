# coding=utf-8
import json
import lzstring
import pprint
import six


if __name__ == '__main__':
    x = lzstring.LZString()

    s = u'Žluťoučký kůň úpěl ďábelské ódy!'

    # generated with original js lib
    jsLzStringBase64 = 'r6ABsK6KaAD2aLCADWBfgBPQ9oCAlAZAvgDobEARlB4QAEOAjAUxAGd4BL5AZ4BMBPAQiAAA'
    jsLzStringBase64Json = 'N4Ig5gNg9gzjCGAnAniAXKALgS0xApuiPgB7wC2ADgQASSwIogA0IA4tHACLYBu6WXASIBlFu04wAMthiYBEhgFEAdpiYYQASS6i2AWSniRURJgCCMPYfEcGAFXyJyozPBUATJB5pt8Kp3gIbAAvfB99JABrAFdKGil3MBj4MEJWcwBjRCgVZBc0EBEDIwyAIzLEfH5CrREAeRoADiaAdgBONABGdqaANltJLnwAMwVKJHgicxpyfDcAWnJouJoIJJS05hoYmHCaTCgabPx4THxZlfj1lWTU/BgaGBjMgAsaeEeuKEyAISgoFEAHSDBgifD4cwQGBQdAAbXYNlYAA0bABdAC+rDscHBhEKy0QsUoIAxZLJQAAA=='

    six.print_('String for encode: ' + s)
    six.print_()

    six.print_('Compress to base64:')
    base2 = x.compressToBase64(s)
    six.print_('result:    ' + base2)
    six.print_('result js: ' + jsLzStringBase64)
    six.print_('equals:    ' + str(base2 == jsLzStringBase64))

    six.print_()

    six.print_('Decompress from base64:')
    six.print_('result:         ' + x.decompresFromBase64(base2))
    six.print_('result from js: ' + x.decompresFromBase64(jsLzStringBase64))

    six.print_()

    jsonString = '{"glossary":{"title":"example glossary","GlossDiv":{"title":"S","GlossList":{"GlossEntry":{"ID":"SGML","SortAs":"SGML","GlossTerm":"Standard Generalized Markup Language","Acronym":"SGML","Abbrev":"ISO 8879:1986","GlossDef":{"para":"A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso":["GML","XML"]},"GlossSee":"markup"}}}}}'

    six.print_('Compress json to base64:')
    jresult = x.compressToBase64(jsonString)

    six.print_('result:    ' + jresult)
    six.print_()
    six.print_('result js: ' + jsLzStringBase64Json)
    six.print_()
    six.print_('equals: ' + str(jresult == jsLzStringBase64Json))

    six.print_()

    six.print_('Decompress json from base64:')
    pprint.pprint(json.loads(x.decompresFromBase64(jsLzStringBase64Json)))
