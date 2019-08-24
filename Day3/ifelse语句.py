

def main(face):

    if face=="1":
        face_str="A"
    elif face=="11":
        face_str="Q"
    else:
        face_str=face

    print(face_str)

if __name__=="__main__":
    main("1")
    main("11")
    main("3")
    main("11")

