#คืนค่าเฉลี่ยของคะแนน ปัดเศษ 2 ตำแหน่ง ถ้าลิสต์ว่างคืน 0
def average(scores):
   return sum(scores) / len(scores) if scores else 0

def is_pass(score):
    return score >= 50

#22222
def is_pass(score):
    return score >= 50

#แปลงคะแนน (0-100) เป็นเกรด ถ้าอยู่นอกช่วงจะเกิด ValueError
def to_grade(score):
    if score<0 or score>100:
        raise ValueError("คะแนนต้องอยู่ในช่วง 0 - 100")
    elif score>=80:
        return "A"
    elif score>=70:
        return "B"
    elif score>=60:
        return "C"
    elif score>=50:
        return "D"
    else:
        return "F"

    

#ผ่านเมื่อได้คะแนนตั้งแต่ 50 ขึ้นไป
def is_pass(score):
    return score>=50

if __name__=="__main__":
    scores=[85,78,71]
    avg=average(scores)
    print(f"คะแนนเเฉลี่ย : {avg}")
    print(f"เกรดที่ได้ : {to_grade(avg)}")