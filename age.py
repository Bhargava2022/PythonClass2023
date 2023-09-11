{\rtf1\ansi\ansicpg1252\cocoartf2708
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Set variable age\
age = int(input("Enter your age: "))\
\
# Check if age is less than 18\
if age < 18:\
    print("You are a minor.")\
\
# Check if age is equal to 18\
elif age == 18:\
    print("Congratulations, you just became an adult!")\
\
# Check if age is greater than 18\
else:\
    print("You are an adult.")\
}