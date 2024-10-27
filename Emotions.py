Emotions = { 
    "happy": {
            "danceability": [0.7, 1.0],
            "Energy": [0.7, 1.0],
            "Valency": [0.5, 1.0],
            "Tempo": [120,200],
            "Liveliness": [0.5, 1.0]
    }, 
    "joyful": {
            "danceability": [0.7, 1.0],
            "Energy": [0.7, 1.0],
            "Valency": [0.5, 1.0],
            "Tempo": [120,200],
            "Liveliness": [0.5, 1.0]
    },
    "sad" : {
        "danceability": [0.0, 0.3],
        "Energy": [0.0, 0.3],
        "Valency": [0.0, 0.5],
        "Tempo": [60,120],
        "Liveliness": [0.0, 0.5]
    },
    "melancholy" : {
        "danceability": [0.0, 0.3],
        "Energy": [0.0, 0.3],
        "Valency": [0.0, 0.5],
        "Tempo": [60,120],
        "Liveliness": [0.0, 0.5]
    },
    "fear" : {
        "danceability": [0.7, 1.0],
        "Energy": [0.7, 1.0],
        "Valency": [0.5, 1.0],
        "Tempo": [80, 140],
        "Liveliness": [0.0, 0.5]
    },
    "anger" : {
        "danceability": [0.7, 1.0],
        "Energy": [0.7, 1.0],
        "Valency": [0.5, 1.0],
        "Tempo": [100, 180],
        "Liveliness": [0.5, 1.0]
    },
    "neutral" : {
        "danceability": [0.7, 1.0],
        "Energy": [0.7, 1.0],
        "Valency": [0.5, 1.0],
        "Tempo": [90, 120],
        "Liveliness": [0.5, 1.0]
    },
    "calm" : {
        "danceability": [0.2, 0.4],
        "Energy": [0.2, 0.4],
        "Valency": [0.6, 0.9],
        "Tempo": [50, 80],
        "Liveliness": [0.2, 0.4]
    },
    "mystery" : {
            "danceability": [0.3, 0.5],
            "Energy": [0.3, 0.7],
            "Valency": [0.0, 0.4],
            "Tempo": [80, 140],
            "Liveliness": [0.2, 0.5]
    },
}
#Define a Function to multiply a scalar by one of these values and return a minimum and maximum
def multiplyEmotion(scalar, emotion):
    min = 0
    max = 1
    print(emotion)
    keys = list(Emotions[emotion].keys());
    minArray = []
    maxArray = []
    for key in keys:
        minArray.append(scalar * Emotions[emotion][key][min])
        maxArray.append(scalar * Emotions[emotion][key][max])
    pairArray = []
    for i in range(len(minArray)):
        pairArray.append([minArray[i], maxArray[i]])
    return pairArray

def addEmotion(emotion1, emotion2):
    min = 0
    min = 1
    keys = list(Emotions[emotion1].keys())
    sumArray = []
    for key in keys:
        sumArray.append = [
            Emotions[emotion1][key][min]+Emotions[emotion2][key][min],
            Emotions[emotion1][key][max]+Emotions[emotion2][key][max]
        ]


    

