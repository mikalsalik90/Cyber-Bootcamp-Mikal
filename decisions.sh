#!/bin/bash

name=Mikal

echo "Welcome to our class quiz $name. There will be 3 questions testing your knowlege on food. each correct answer will be worth one point."
echo "which of these fruit are red? A(Cantaloupes) B(Apples) or C(grapes)."
read choice 
if [ "$choice" = "A" ]; then
echo "Incorrect, Cantaloupes are not red"
elif [ "$choice" = "B" ]; then
echo "Correct! Apples are red"
elif [ "$choice" = "C" ]; then
echo " Are you serious?"
else
echo "invalid response"
fi
echo " Now for the 2nd question, What color is a banana?"
read choice
if [ "$choice" = "Yellow" ]; then
echo "Correct"
else 
echo "you gotta be kidding me!"
fi
echo "Last but not least Which is typically heavier a grape or watermelon?"
read choice
if [ "$choice" = Watermelon ]; then
echo "Correct"
else
echo "Incorrect"
fi


