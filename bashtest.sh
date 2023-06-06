#!/bin/bash
#above shebang
: << 'COMMENT'

COMMENT

#creates file
touch bashtest.sh

echo hello world

ls -l
ls /
#non built-in commands
ls /bin
sleep 1

chmod +x bashtest.sh

#No spaces 
VARIABLENAME="What is your name?"
echo $VARIABLENAME
read NAME
echo Hello $NAME.

#./bashtest.sh runs it

#From bash course
#!/bin/bash
#Program that reads and echos questions
QUESTION1="What's your name?"
QUESTION2="Where are you from?"
QUESTION3="What's your favorite coding website?"
echo -e "\n~~ Questionnaire ~~\n"
echo $QUESTION1
read NAME
echo $QUESTION2
read LOCATION
echo $QUESTION3
read WEBSITE
echo -e "\n"Hello $NAME from $LOCATION. I learned that your favorite coding website is $WEBSITE!


#!/bin/bash
#Program that counts down to zero from a given argument
echo -e "\n"~~ Countdown Timer ~~"\n"
if [[ $1 -gt 0 ]] 
then 
: '
  for (( i = $1; i >= 0; i-- ))
  do
    echo $i
    sleep 1
  done
'
I=$1
while [[ $I -ge 0 ]]
do
echo $I
(( I-- ))
sleep 1
done
else 
  echo Include a positive integer as the first argument. 
fi

: '
bash exercise world cup results table
#! /bin/bash

if [[ $1 == "test" ]]
then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi

# Do not change code above this line. Use the PSQL variable above to query your database.

#CSV
#year,round,winner,opponent,winner_goals,opponent_goals
cat games.csv | while IFS="," read -r YEAR ROUND WINNER OPPONENT WINGOAL OPPGOAL
do
  if [[ $YEAR != 'year' ]]
    then
    WINID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")
    OPPID=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT'")
    if [[ -z $WINID ]]
    then
      INSERT=$($PSQL "INSERT INTO teams (name) VALUES ('$WINNER')")
      WINID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")
    fi
    if [[ -z $OPPID ]]
    then
      INSERT=$($PSQL "INSERT INTO teams (name) VALUES ('$OPPONENT')")
      OPPID=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT'")
    fi
    INSERT=$($PSQL "INSERT INTO games (year,round,winner_id,opponent_id,winner_goals,opponent_goals) VALUES ($YEAR,'$ROUND',$WINID,$OPPID,$WINGOAL,$OPPGOAL)")
  fi
done


'