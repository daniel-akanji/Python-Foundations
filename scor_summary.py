def score_summary(name, a, b, c):
    try:
        scores = {
        score1 := int(a),
        score2 := int(b),
        score3 := int(c)
        }
    
    except:
        return "Invalid score"
    
    for score in scores:
        if score < 0 or score > 100:
            return "Invalid score"
        else:
            Average = (score1 + score2 + score3)/3
            avg = round(Average,2)

    Grade = ""
    if Average >= 90:
        Grade = "A"
    elif Average >= 80:
        Grade = "B"
    elif Average >= 70:
        Grade = "C"
    else:
        Grade = "F"
    
    return (f"Student: {name}\nAverage: {avg}\nGrade: {Grade}")
