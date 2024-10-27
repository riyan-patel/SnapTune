import compute_face_exp
import compute_color
import compute_caption
import compute_mood
import Emotions

def calculate_music_attributes(image_path):
    def addRanges(arr1, arr2):
        minVal = 0
        maxVal = 1
        finalArr = []
        for i in range(len(arr1)):
            finalArr.append([arr1[i][minVal] + arr2[i][minVal], arr1[i][maxVal] + arr2[i][maxVal]])
        return finalArr

    def multiplyRange(scalar, arr):
        minVal = 0
        maxVal = 1
        finalArr = []
        for i in range(len(arr)):
            finalArr.append([scalar * arr[i][minVal], scalar * arr[i][maxVal]])
        return finalArr

    # Compute everything
    ColorPalette = compute_color.compute_color(image_path)
    ImgMood = compute_mood.compute_mood(image_path)
    ImgCaption = compute_caption.compute_caption(image_path)
    FaceCount, FaceExp = compute_face_exp.compute_face_exp(image_path)

    # Assign emotional values
    
    if (ImgMood == "nostalgic" or ImgMood == "mysterious"):
        moodBoolean = True
        ImgMood = "happy"
        MoodScore = Emotions.Emotions["happy"]
    else: 
        MoodScore = Emotions.Emotions[ImgMood]
        moodBoolean = False
    if FaceCount != 0:
        FaceScore = Emotions.Emotions[FaceExp]
    ColorMap = ["happy", "sad", "neutral"]
    ColorScore = addRanges(
        addRanges(Emotions.multiplyEmotion(ColorPalette[0], ColorMap[0]), Emotions.multiplyEmotion(ColorPalette[1], ColorMap[1])),
        Emotions.multiplyEmotion(ColorPalette[2], ColorMap[2])
    )

    # Weights
    if(moodBoolean):
        MoodWeightPerson = 0.0
        FacialWeightPerson = 0.7
        ColorWeightPerson = 0.3
        MoodWeightObject = 0.0
        FacialWeightObject = 0.0
        ColorWeightObject = 1.0
    else:
        MoodWeightPerson = 0.3
        FacialWeightPerson = 0.6
        ColorWeightPerson = 0.1
        MoodWeightObject = 0.65
        FacialWeightObject = 0.0
        ColorWeightObject = 0.35

    # Calculate
    if FaceCount == 0:
        FinalArray = addRanges(Emotions.multiplyEmotion(MoodWeightObject, ImgMood), multiplyRange(ColorWeightObject, ColorScore))
    else:
        FinalArray = addRanges(
            addRanges(Emotions.multiplyEmotion(MoodWeightPerson, ImgMood), multiplyRange(ColorWeightPerson, ColorScore)),
            Emotions.multiplyEmotion(FacialWeightPerson, FaceExp)
        )

    # Extract ranges
    danceabilityRange = FinalArray[0]
    energyRange = FinalArray[1]
    valenceRange = FinalArray[2]
    tempoRange = FinalArray[3]
    LivelinessRange = FinalArray[4]

    # Return the ranges as a dictionary
    return {
        "danceabilityRange": danceabilityRange,
        "energyRange": energyRange,
        "valenceRange": valenceRange,
        "tempoRange": tempoRange,
        "LivelinessRange": LivelinessRange
    } , moodBoolean
