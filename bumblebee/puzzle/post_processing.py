import string

from AviaryFX.AviaryFX import AviaryFX

from bumblebee import settings

FILTER_MAP = {"comic":
                    {"key":20,
                    "params":[
                       {"id" : "Color Count", "value" : "12"},
                       {"id" : "Saturation", "value" : "1"},
                       {"id" : "Curve Smoothing", "value" : "4"},
                       {"id" : "Posterization", "value" : "12"},
                       {"id" : "Pattern Channel", "value" : "7"},
                       {"id" : "Pattern Threshold", "value" : "100"},
                       {"id" : "Pattern Scale", "value" : "1"},
                       {"id" : "Pattern Angle", "value" : "0.3"},
                       {"id" : "Pattern Type", "value" : "0"}
                       ]
                 },
              "bad ass":
                   {"key":24,
                    "params":[
                       {"id" : "Gradient Seed", "value" : "409244424"},
                       {"id" : "Black Intensity", "value" : "0.9822179947239853"},
                       {"id" : "White Intensity", "value" : "0.8970553915475159"},
                       {"id" : "Contrast", "value" : "29.833313950997148"},
                       {"id" : "Black Threshold", "value" : "30"},
                       {"id" : "White Threshold", "value" : "24"}
                       ]
                    },
              "blur":
                    {"key":15,
                    "params":[
                       {"id" : "Center", "value" : "0,3"},
                       {"id" : "Inner Limit", "value" : "0.33"},
                       {"id" : "Outer Limit", "value" : "0.9"},
                       {"id" : "Blur Radius", "value" : "3.28"},
                       {"id" : "Radius Factor", "value" : "2.44"},
                       {"id" : "Radius Gamma", "value" : "1.316"}
                    ]
                }
            }


def process(file, extension, filter):
    aviaryfx = AviaryFX(settings.AVIARY_API_KEY, settings.AVIARY_API_SECRET)
    #filters = aviaryfx.getFilters()
    file_path = file.file.path
    response = aviaryfx.upload(file_path)
    uploaded_file_url = response['url']
    
    filter_name = string.lower(filter.name)
    if FILTER_MAP.has_key(filter_name):
        filter = FILTER_MAP[filter_name]
        filter_id = filter['key']
        filter_params = filter['params']
        extension = string.replace(extension, '.', '')
        
        # Aviary specific parameters
        backgroundColor = "0xFFFFFFFF"
        format = extension
        quality = "100"
        scale = "1"
        width = "400"
        height = "300"
        filepath = uploaded_file_url
        filterid = filter_id
        renderParameters = filter_params
        renderResponse = aviaryfx.render(backgroundColor, format, quality, scale, filepath, filterid, width, height, renderParameters)
    else:
        pass
    return (renderResponse['url'], uploaded_file_url,)