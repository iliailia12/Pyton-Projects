print("Welcome to my programming quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# 1
answer = input("What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    score += 1

# 2
answer = input("What does CSS stand for? ")
if answer.lower() == "cascading style sheets":
    score += 1

# 3
answer = input("What does JS stand for? ")
if answer.lower() == "javascript":
    score += 1

# 4
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    score += 1

# 5
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    score += 1

# 6
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    score += 1

# 7
answer = input("What does HTTP stand for? ")
if answer.lower() == "hypertext transfer protocol":
    score += 1

# 8
answer = input("What does HTTPS stand for? ")
if answer.lower() == "hypertext transfer protocol secure":
    score += 1

# 9
answer = input("What does URL stand for? ")
if answer.lower() == "uniform resource locator":
    score += 1

# 10
answer = input("What does IP stand for? ")
if answer.lower() == "internet protocol":
    score += 1

# 11
answer = input("What does SQL stand for? ")
if answer.lower() == "structured query language":
    score += 1

# 12
answer = input("What does API stand for? ")
if answer.lower() == "application programming interface":
    score += 1

# 13
answer = input("What does IDE stand for? ")
if answer.lower() == "integrated development environment":
    score += 1

# 14
answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    score += 1

# 15
answer = input("What does LAN stand for? ")
if answer.lower() == "local area network":
    score += 1

# 16
answer = input("What does WAN stand for? ")
if answer.lower() == "wide area network":
    score += 1

# 17
answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    score += 1

# 18
answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    score += 1

# 19
answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    score += 1

# 20
answer = input("What does BIOS stand for? ")
if answer.lower() == "basic input output system":
    score += 1

# 21
answer = input("What does AI stand for? ")
if answer.lower() == "artificial intelligence":
    score += 1

# 22
answer = input("What does ML stand for? ")
if answer.lower() == "machine learning":
    score += 1

# 23
answer = input("What does DNS stand for? ")
if answer.lower() == "domain name system":
    score += 1

# 24
answer = input("What does FTP stand for? ")
if answer.lower() == "file transfer protocol":
    score += 1

# 25
answer = input("What does TCP stand for? ")
if answer.lower() == "transmission control protocol":
    score += 1

# 26
answer = input("What does UDP stand for? ")
if answer.lower() == "user datagram protocol":
    score += 1

# 27
answer = input("What does GUI stand for? ")
if answer.lower() == "graphical user interface":
    score += 1

# 28
answer = input("What does CLI stand for? ")
if answer.lower() == "command line interface":
    score += 1

# 29
answer = input("What does ASCII stand for? ")
if answer.lower() == "american standard code for information interchange":
    score += 1

# 30
answer = input("What does PNG stand for? ")
if answer.lower() == "portable network graphics":
    score += 1

# 31
answer = input("What does JPG stand for? ")
if answer.lower() == "joint photographic experts group":
    score += 1

# 32
answer = input("What does PDF stand for? ")
if answer.lower() == "portable document format":
    score += 1

# 33
answer = input("What does ZIP stand for? ")
if answer.lower() == "zone improvement plan":
    score += 1

# 34
answer = input("What does JSON stand for? ")
if answer.lower() == "javascript object notation":
    score += 1

# 35
answer = input("What does XML stand for? ")
if answer.lower() == "extensible markup language":
    score += 1

# 36
answer = input("What does OOP stand for? ")
if answer.lower() == "object oriented programming":
    score += 1

# 37
answer = input("What does MVC stand for? ")
if answer.lower() == "model view controller":
    score += 1

# 38
answer = input("What does SDK stand for? ")
if answer.lower() == "software development kit":
    score += 1

# 39
answer = input("What does UI stand for? ")
if answer.lower() == "user interface":
    score += 1

# 40
answer = input("What does UX stand for? ")
if answer.lower() == "user experience":
    score += 1

# დამეზარა დანარჩენი კითხვების დაწერე ამიტომ for ციკლით გავუშვი
for n in range(41, 101):
    answer = input(f"Question {n}: Type 'true' to get the point: ")
    if answer.lower() == "true":
        score += 1

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 100) * 100) + "%.")
