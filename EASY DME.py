#---------------------------------------------------
# Programme Name: EASY DME (Lower-Back Assesment)
# This demo program simplifies DME and health support products for the public by utilizing...
#...a self self diagnostic approach and intuitive systems.
'''
We all know it's best to see a medical or health provider when we encounter health problems. Specifically ones
dealing with the lower back,shoulder and kneck.

Although when most people encounter pain... often times they try to play doctor in lieu of getting evaluated by a
certified provider.

Easy DME supports the user in making the possibly best subjective assesment in regards to the appropriate DME
or health products(i.e - kneck brace, back brace, knee brace..etc) without FIRST visiting a certified provider.

'''
# Written by Darling Ngoh, May 2022.
# Anyone may freely copy or modify this program with credit from the source code.
#---------------------------------------------------


#scoring scale:
'''
1 - light
2 - moderate
3 - mod to severe
4 - severe

With total score of 39 given 11 scored questions
Slighty-Increased risk vs Increased Risk will be ditermined based on the score: Slightly-increased risk <= 19 and highly-increased risk >= 20

Theory:
    given the scoring system, one should be able to accertain a subjective yet qualitative method
    for defining a slightly increased risk disposition to an increased risk condition. Bearing in
    mind the questions asked are constructive and effective in regards to the scoring scale.

    Hence a high accuracy in a self diagnostic method will be the outcome.
'''

import sys

def welcome_message(): #initial welcome message giving user info and instructions on proper program usage
    print("Welcome to EASY DME: \nThe goal of the programme is to help you in making an optimal product support decision\
 in regards to your assesment given your region of complaint.\n")
    print("Version: 1.0 [---Online Test - Back Pain Assestment & Results----]\n\
*This programme is intended for public use: Anyone may use it freely*\n\n")
    print("INFO:\n*you will be using the keyboard options(ie - A, B, C, D and E) to progress through the program.\n\n\
*Remember to press the 'Enter' key once you would like to submit your answer*")
    print("-------------------------------------------------------------------------------------------------\n\n")


def main():
    #initializing variables
    score = 0
    exit_msg = ("Q")
    user_age_key = {"A": "Under 40", "B":"Between 40-55", "C":"Over 55"}
    user_gender_key = {"A": "Female", "B":"Male"}
    user_deformities_key = {"A": "Yes, scoliosis", "B":"Yes, hollow back, rounded back, flat back", "C":"Yes, different leg lengths", "D": "No, not known"}
    user_DegenerativeDisease_key = {"A": "Yes, prolapsed intervertebral disc","B":"Yes, osteoarthritis", "C":"No, not known"}
    user_bp_sensations_key = {"A": "Sharp, stabbing, tingling, or numbness","B":" mild-ache or throb", "C":"Slight-ache", "D":"N/A"}
    user_BMI_key = {"A":"Yes, very (BMI>34)", "B":"Yes, moderately (BMI>28)" , "C":"Yes, slightly (BMI>25)", "D":"No","E": "help figuring out your BMI"}
    user_backpain_frequency_key = {"A":"Daily","B":"Every 3 or 4 days","C":"A few days a month","D":"A few days a year","E":"Never"}
    user_bp_activity_key = {"A":"During certain movements (e.g. lifting heavy objects)","B":"After sitting or lying down for a long time","C":"After walking or running for a long time","D":"The pain occurs sporadically"}
    user_bp_workstress_key = {"A":"Very stressful due to physically demanding activities","B":"One-sided stress due to sitting or standing for long periods","C":"Low stress due to changing position often at work"}
    user_bp_emotions_key = {"A":"Yes, permanent severe stress","B":"Yes, often stress","C":"Yes, occasional stress","D":"No"}
    user_bp_support_key = {"A":"Several times a week","B":"At least once a week","C":"Rarely","D":"Never"}
    user_provider_consent_key = {"A": "Yes, claim my discount and continue to recommended product support", "B": "Not right now, continue to recommended product support"}
    
    highly_increased_risk = ("\n\nYour assessment is: HIGHLY-INCREASED RISK\n\nExplanations about this assessment\n\n\
Back pain is often caused by overworked muscles and ligaments or wear and tear of the spine and the intervertebral discs. \
There are many reasons for this: a one-sided posture while working, a lack of physical exercise or the wrong movements and emotional stresses in day-to-day life.\n\n\
Guide to back treatment: Here's how to get your back fit again... \n\n")

    slightly_increased_risk = ("\n\nYour assessment is: SLIGHTLY-INCREASED RISK\n\nExplanations about this assessment\n\nThere are many reasons for back pain. It often develops as a result of remaining for long periods in the same position or because of too little exercise or the wrong movements.\
 A sedentary job is often a contributory factor for pain in the back. Psychological stresses in day-to-day life or pressure to perform at work or strife with the partner can have negative effects on the state of your back.\
  The result: your body grows tense, the muscles lose their normal elasticity, grow hard and hurt.\n\n\
  However, you can prevent back pain before it gets a chance develop. Pursue back-friendly sports such as power walking, swimming or cycling. Regular sporting activities strengthen the back muscles and help support the spinal column better.\
  Also make sure you have enough relaxation during the day, for example, with soothing massages, autogenic training and meditation exercises. A healthy diet, particularly in association with obesity, is an important precondition for a healthy back.\n\n\
  Prevention – tips for a strong back.")

        
    #calling funtions
    welcome_message()
    while True:
        to_start_or_not_to_start = input("Have you EVER experienced lower back pain?\n\nPress Y-(yes I do, continue program) or N-(no I do not, exit program)\n\n").upper()
        if to_start_or_not_to_start == "N":
            print("\n\nLooks like you're damn healthy, awesome!! This program was not intended for you, Goodbye!! :)")
            sys.exit()
        elif to_start_or_not_to_start == "Y":
            print("\n\nAwesome, let's begin!\n\n")
        else:
            print("Oops thats not a valid option, try again. Press: Y, or N\n")
            continue
        break
   
    while True: #Question 1 - keep looping through until user answer is appropriate choice
        try:#function for ease of handling exceptions/errors
            print("-------------------------------------------------------------------------------------")
            user_age = input("\nQuestion: 1/11... Press 'Q' anytime to EXIT the program.\
\n\nPlease give your age:*\n\n[A:] Under 40\n[B:] Between 40-55\n[C:] Over 55 \n\n").upper()
            
            if user_age == exit_msg:#ensure user can exit program at anytime
                print("\nGOODBYE!!")
                exit
            elif user_age == "A": #approriate user option function
                score += 1 #score   
            elif user_age == "B":
                score += 2#score 
            elif user_age == "C":
                score += 3#score 
            else:#user must use appropriate options before moving onto the next question
                print("Oops thats not a valid option, try again. Press: A , B , or C\n")
                continue
        except:
            error = sys.exc_info()
            print(error[0:9])
            print("Looks like something went wrong.. one sec!")
        try:
            print("\n\nUser Answer: ", user_age_key[user_age])    
            print("\n-------------------------------------------------------------------------------------")
            print("Your risk assesement: ", score)
        except KeyError:
            print("Program Exit Successful")
            sys.exit()
        break
    
    while True: #Question 2
        try:
            print("-------------------------------------------------------------------------------------")
            user_gender = input("\nQuestion: 2/11... Press 'Q' anytime to EXIT the program.\
\n\nPlease give your gender:*\n\n[A:] Female\n[B:] Male\n\n").upper()
            
            if user_gender == exit_msg:
                print("\nGOODBYE!!")
                exit
            elif user_gender == "A":
                score += 1  
            elif user_gender == "B":
                score += 1
            else:
                print("Oops thats not a valid option, try again. Press: A or B\n")
                continue
        except:
            error = sys.exc_info()
            print(error[0:9])
            print("Looks like something went wrong.. one sec!")

        try:
            print("\n\nUser Answer: ", user_gender_key[user_gender])    
            print("\n-------------------------------------------------------------------------------------")
            print("Your risk assesement score: ", score)
        except KeyError:
            print("Program Exit Successful")
            sys.exit()
        break
    
    while True: #Question 3
        try:
            print("-------------------------------------------------------------------------------------")
            user_deformities = input("\nQuestion: 3/11... Press 'Q' anytime to EXIT the program.\
\n\nDo you suffer from any anatomical deformities?*\n(e.g. scoliosis, different leg lengths, \
hollow back, rounded back or similar conditions)*\n\n[A:] Yes, scoliosis\n[B:] Yes, hollow back, rounded back, flat back\n\
[C:] Yes, different leg lengths \n[D:] No, not known\n\n").upper()
            
            if user_deformities == exit_msg:
                print("\nGOODBYE!!")
                exit
            elif user_deformities == "A": 
                score += 2    
            elif user_deformities == "B":
                score += 3
            elif user_deformities == "C":
                score += 2
            elif user_deformities == "D":
                score += 1
            else:
                print("Oops thats not a valid option, try again. Press: A , B , C or D\n")
                continue
        except:
            error = sys.exc_info()
            print(error[0:9])
            print("Looks like something went wrong.. one sec!")

        try:
            print("\n\nUser Answer: ", user_deformities_key[user_deformities])    
            print("\n-------------------------------------------------------------------------------------")
            print("Your risk assesement score: ", score)
        except KeyError:
            print("Program Exit Successful")
            sys.exit()
        break
    
    while True: #Question 4
        try:
            print("-------------------------------------------------------------------------------------")
            user_DegenerativeDisease = input("\nQuestion: 4/11... Press 'Q' anytime to EXIT the program.\
\n\nDo you suffer from degenerative diseases of the spine?*\n(e.g. prolapsed intervertebral disc, osteoarthritis or similar conditions)*\n\n\
[A:] Yes, prolapsed intervertebral disc (i.e - herniated disk or spine compression)\n[B:] Yes, osteoarthritis (i.e - degenerative joint disease)\n\
[C:] No, not known\n\n").upper()
            
            if user_DegenerativeDisease == exit_msg:
                print("\nGOODBYE!!")
                exit
            elif user_DegenerativeDisease == "A": 
                score += 4   
            elif user_DegenerativeDisease == "B":
                score += 3
            elif user_DegenerativeDisease == "C":
                score += 1

            else:
                print("Oops thats not a valid option, try again. Press: A , B , or C\n")
                continue
        except:
            error = sys.exc_info()
            print(error[0:9])
            print("Looks like something went wrong.. one sec!")

        try:
            print("\n\nUser Answer: ", user_DegenerativeDisease_key[user_DegenerativeDisease])    
            print("\n-------------------------------------------------------------------------------------")
            print("Your risk assesement score: ", score)
        except KeyError:
            print("Program Exit Successful")
            sys.exit()   
        break
    while True: #Question 5
        try:
            print("-------------------------------------------------------------------------------------")
            user_BMI = input("\nQuestion: 5/11... Press 'Q' anytime to EXIT the program.\
\n\nAre you overweight?*\n(Calculation of the Body Mass Index (BMI): Body weight in kg X(height in m2)*\n\n\
[A:] Yes, very (BMI>34)\n[B:] Yes, moderately (BMI>28)\n\
[C:] Yes, slightly (BMI>25)\n[D:] No\n[E:] *if you need help figuring out your BMI\n\n").upper()
            
            if user_BMI == exit_msg:
                print("\nGOODBYE!!")
                exit
            elif user_BMI == "A": 
                score += 4   
            elif user_BMI == "B":
                score += 3
            elif user_BMI == "C":
                score += 2
            elif user_BMI == "D":
                score += 0
            elif user_BMI == "E":
                print("Let's go ahead and find out what your BMI is")
                user_weight_lbs = int(input("What is your weight in pounds(lbs) - Type number:"))
                user_weight_kg = float((user_weight_lbs) * 0.45359237) #converting lbs to kg
                user_height_foot = float(input("What is your height? First input the feet, we will ask for inches after: - Type number:"))
                user_height_inches = float(input("Next input the second part of your height which should be the inches: - Type number:"))
                user_weight_m2 = float((((user_height_foot*12 + user_height_inches)*0.0254)**2))#converting feet to inches and inches to meters and meters to m2
                print("\n\nYour BMI Score: ", user_weight_kg/user_weight_m2) #formulat for BMI
                continue
            else:
                print("Oops thats not a valid option, try again. Press: A , B , C, D or E\n")
                continue
        except:
            error = sys.exc_info()
            print(error[0:9])
            print("Looks like something went wrong.. one sec!")

        try:
            print("\n\nUser Answer: ", user_BMI_key[user_BMI])    
            print("\n-------------------------------------------------------------------------------------")
            print("Your risk assesement score: ", score)
        except KeyError:
            print("Program Exit Successful")
            sys.exit()   
        break
    
    while True: #Question 6
        try:
            print("-------------------------------------------------------------------------------------")
            user_backpain_frequency = input("\nQuestion: 6/11... Press 'Q' anytime to EXIT the program.\
\n\nHow often do you suffer from back pain?*\n\n\
[A:] Daily\n[B:] Every 3 or 4 days\n\
[C:] A few days a month\n[D:] A few days a year\n[E:] Never\n\n").upper()
            
            if user_backpain_frequency == exit_msg:
                print("\nGOODBYE!!")
                exit
            elif user_backpain_frequency == "A": 
                score += 4  
            elif user_backpain_frequency == "B":
                score += 3
            elif user_backpain_frequency == "C":
                score += 2
            elif user_backpain_frequency == "D":
                score += 1
            elif user_backpain_frequency == "E":
                score += 0
            else:
                print("Oops thats not a valid option, try again. Press: A , B , C, D or E\n")
                continue
        except:
            error = sys.exc_info()
            print(error[0:9])
            print("Looks like something went wrong.. one sec!")

        try:
            print("\n\nUser Answer: ", user_backpain_frequency_key[user_backpain_frequency])    
            print("\n-------------------------------------------------------------------------------------")
            print("Your risk assesement score: ", score)
        except KeyError:
            print("Program Exit Successful")
            sys.exit()   
        break
    while True: #Question 7
        try:
            print("-------------------------------------------------------------------------------------")
            user_bp_activity = input("\nQuestion: 7/11... Press 'Q' anytime to EXIT the program.\
\n\nIf you suffer from back pain: when does the pain occur most often?*\n\n\
[A:] During certain movements (e.g. lifting heavy objects)\n[B:] After sitting or lying down for a long time\n\
[C:] After walking or running for a long time\n[D:] The pain occurs sporadically\n\n").upper()
            
            if user_bp_activity == exit_msg:
                print("\nGOODBYE!!")
                exit
            elif user_bp_activity == "A": 
                score += 4  
            elif user_bp_activity == "B":
                score += 2
            elif user_bp_activity == "C":
                score += 2
            elif user_bp_activity == "D":
                score += 3
            else:
                print("Oops thats not a valid option, try again. Press: A , B , C or D\n")
                continue
        except:
            error = sys.exc_info()
            print(error[0:9])
            print("Looks like something went wrong.. one sec!")

        try:
            print("\n\nUser Answer: ", user_bp_activity_key[user_bp_activity])    
            print("\n-------------------------------------------------------------------------------------")
            print("Your risk assesement score: ", score)
        except KeyError:
            print("Program Exit Successful")
            sys.exit()   
        break
    while True: #Question 8
        try:
            print("-------------------------------------------------------------------------------------")
            user_bp_sensations = input("\nQuestion: 8/11... Press 'Q' anytime to EXIT the program.\
\n\nIf you suffer from back pain: What is the form of pain and sensation?*\n\n\
[A:] Sharp, stabbing, tingling, or numbness\n[B:] mild-ache or throb\n\
[C:] Slight-ache\n[D:] N/A\n\n").upper()
            
            if user_bp_sensations == exit_msg:
                print("\nGOODBYE!!")
                exit
            elif user_bp_sensations == "A": 
                score += 4  
            elif user_bp_sensations == "B":
                score += 3
            elif user_bp_sensations == "C":
                score += 2
            elif user_bp_sensations == "D":
                score += 0
            else:
                print("Oops thats not a valid option, try again. Press: A , B , C or D\n")
                continue
        except:
            error = sys.exc_info()
            print(error[0:9])
            print("Looks like something went wrong.. one sec!")

        try:
            print("\n\nUser Answer: ", user_bp_sensations_key[user_bp_sensations])    
            print("\n-------------------------------------------------------------------------------------")
            print("Your risk assesement score: ", score)
        except KeyError:
            print("Program Exit Successful")
            sys.exit()   
        break
    while True: #Question 9
        try:
            print("-------------------------------------------------------------------------------------")
            user_bp_workstress = input("\nQuestion: 9/11... Press 'Q' anytime to EXIT the program.\
\n\nHow stressful is your job for your back?*\n\n\
[A:] Very stressful due to physically demanding activities\n[B:] One-sided stress due to sitting or standing for long periods\n\
[C:] Low stress due to changing position often at work\n\n").upper()
            
            if user_bp_workstress == exit_msg:
                print("\nGOODBYE!!")
                exit
            elif user_bp_workstress == "A": 
                score += 4  
            elif user_bp_workstress == "B":
                score += 3
            elif user_bp_workstress == "C":
                score += 2
            else:
                print("Oops thats not a valid option, try again. Press: A , B , or C\n")
                continue
        except:
            error = sys.exc_info()
            print(error[0:9])
            print("Looks like something went wrong.. one sec!")

        try:
            print("\n\nUser Answer: ", user_bp_workstress_key[user_bp_workstress])    
            print("\n-------------------------------------------------------------------------------------")
            print("Your risk assesement score: ", score)
        except KeyError:
            print("Program Exit Successful")
            sys.exit()   
        break
    while True: #Question 10
        try:
            print("-------------------------------------------------------------------------------------")
            user_bp_emotions = input("\nQuestion: 10/11... Press 'Q' anytime to EXIT the program.\
\n\nDo you suffer from severe emotional or occupational stress?*\n\n\
[A:] Yes, permanent severe stress\n[B:] Yes, often stress\n\
[C:] Yes, occasional stress\n[D:] No\n\n").upper()
            
            if user_bp_emotions == exit_msg:
                print("\nGOODBYE!!")
                exit
            elif user_bp_emotions == "A": 
                score += 4  
            elif user_bp_emotions == "B":
                score += 3
            elif user_bp_emotions == "C":
                score += 2
            elif user_bp_emotions == "D":
                score += 1
            else:
                print("Oops thats not a valid option, try again. Press: A , B , C or D\n")
                continue
        except:
            error = sys.exc_info()
            print(error[0:9])
            print("Looks like something went wrong.. one sec!")

        try:
            print("\n\nUser Answer: ", user_bp_emotions_key[user_bp_emotions])    
            print("\n-------------------------------------------------------------------------------------")
            print("Your risk assesement score: ", score)
        except KeyError:
            print("Program Exit Successful")
            sys.exit()   
        break
    while True: #Question 11
        try:
            print("-------------------------------------------------------------------------------------")
            user_bp_support = input("\nQuestion: 11/11... Press 'Q' anytime to EXIT the program.\
\n\nHow often do you do sport to stabilise your back (strength training, exercises, yoga, swimming)?*\n\n\
[A:] Several times a week\n[B:] At least once a week\n\
[C:] Rarely\n[D:] Never\n\n").upper()
            
            if user_bp_support == exit_msg:
                print("\nGOODBYE!!")
                exit
            elif user_bp_support == "A": 
                score += 1  
            elif user_bp_support == "B":
                score += 2
            elif user_bp_support == "C":
                score += 3
            elif user_bp_support == "D":
                score += 4
            else:
                print("Oops thats not a valid option, try again. Press: A , B , C or D\n")
                continue
        except:
            error = sys.exc_info()
            print(error[0:9])
            print("Looks like something went wrong.. one sec!")

        try:
            print("\n\nUser Answer: ", user_bp_support_key[user_bp_support])    
            print("\n-------------------------------------------------------------------------------------")
            print("Your risk assesement score: ", score)
        except KeyError:
            print("Program Exit Successful")
            sys.exit()   
        break
    
    print("\n.\n.\n.\n.\n.\n.\n.\nCONGRATULATIONS!! ALL FINISHED, IT'S TIME TO GET YOUR ASSESMENT ALONG WITH RESOURCES FOR NEXT STEPS IN YOUR JOURNEY")
    print("--------------------------------------------------------------------------------------------------------------------\n")
    print("Your Final risk assesment score: ", score)
    print("What a normal/healthy risk assesment score should be around: 10-15")
    print("\n\nPRIVACY POLICY*\n\
I consent to the use of my personal data for processing my enquiry in compliance with the privacy policy. I am aware that, \
depending on my country of origin and my enquiry, my data will be forwarded to other medi offices or medi agents, in order to \
answer my enquiry.")
    print(input("\n\nPress Enter to continue to resourcouces:..."))

    print("--------------------------------------------------------------------------------------------------------------------\n")

    def assesment_condition(): #this funtion prints out assestment info based on user score
        if score >= 20:
            print(highly_increased_risk)
        elif score <= 19:
            print(slightly_increased_risk)

    assesment_condition() #calling funct.
    print(input("\n\nPress Enter to continue:..."))
    
    
    
    def provider_or_product(): #this function finds out if user would like to be paired with a certified health provider near user location. The user is also sent a helfpful PDF guide along with DME recommendation
        if score >= 20:
            print("\n-------------------------------------------------------------------------------------")
            print("\nGiven your assesment and symptionms - dealing with [%s] pain, [%s ]; we would recommend you get further support and assisance from a certiefied Health/Medical provider. \
EASY DME has partnered up with providers in your network to offer you discounted visit rates (as low as $0) in order to encourage you to continue the next step of your health journey\
" %(user_bp_sensations_key[user_bp_sensations],user_backpain_frequency_key[user_backpain_frequency]))
            while True:
                try:
                    print("-------------------------------------------------------------------------------------")
                    user_provider_consent = input("\nPress 'Q' anytime to EXIT the program.\
        \n\nWould you like for EASY DME to partner you up with a certified provider near you at a discount?*\n\n(NOTICE: Discounts are valid for upto 5 months after purchase)*\n\
[A:] Yes, claim my discount and continue to recommended product support\n[B:] Not right now, continue to recommended product support\n\n\
").upper()
                    
                    if user_provider_consent == exit_msg:
                        print("\nGOODBYE!!")
                        exit
                    elif user_provider_consent == "A": 
                        print("Awesome, let's get you taken care of...\n")
                        user_number_consent = input("What is the best number to reach you: ")
                        user_email_consent = input("Lastly what is the best email address to reach you: ")
                        print(user_number_consent, user_email_consent)
                        print ("\nThank you, our team is working on getting you seen by a provider at a low cost, or possibly FREE.\n\n\
Expect an email or call from EASY DME within the next couple of days.\n[NOTICE:]*A recomended product support from EASY DME MUST be purchased to claim discount*")
                    elif user_provider_consent == "B":
                        print("Okay no worries, you can always claim your discount once your product support has been purchased. Whether tomorrow or 5 months down the line.\n")
                        user_email_consent = input("What is the best email address to reach you in order to send your preventative guide and further resources: ")
                        print(user_email_consent)
                    else:
                        print("Oops thats not a valid option, try again. Press: A , or B \n")
                        continue
                except:
                    error = sys.exc_info()
                    print(error[0:9])
                    print("Looks like something went wrong.. one sec!")

                try:
                    print("\n\nUser Answer: ", user_provider_consent_key[user_provider_consent])
                    print("\n-------------------------------------------------------------------------------------")
                except KeyError:
                    print("Program Exit Successful")
                    sys.exit()   
                break
        if score <= 19:
            print("\n-------------------------------------------------------------------------------------")
            print("\nGiven your assesment and symptionms - dealing with [%s] pain, [%s ]; we would recommend you start working on preventative measures. \
\
" %(user_bp_sensations_key[user_bp_sensations],user_backpain_frequency_key[user_backpain_frequency]))
            while True:
                try:
                    print("-------------------------------------------------------------------------------------")
                    user_provider_consent = input("\nPress 'Q' anytime to EXIT the program.\
        \n\nWould you like for EASY DME to partner you up with a certified provider near you at a discount?*\n\n(NOTICE: Discounts are valid for upto 5 months after purchase)*\n\
[A:] Yes, claim my discount and continue to recommended product support\n[B:] Not right now, continue to recommended product support\n\n\
").upper()
                    
                    if user_provider_consent == exit_msg:
                        print("\nGOODBYE!!")
                        exit
                    elif user_provider_consent == "A": 
                        print("Awesome, let's get you taken care of...\n")
                        user_number_consent = input("What is the best number to reach you: ")
                        user_email_consent = input("Lastly what is the best email address to reach you: ")
                        print(user_number_consent, user_email_consent)
                        print ("\nThank you, our team is working on getting you seen by a provider at a low cost, or possibly FREE.\n\n\
Expect an email or call from EASY DME within the next couple of days.\n[NOTICE:]*A recomended product support from EASY DME MUST be purchased to claim discount*")
                    elif user_provider_consent == "B":
                        print("Okay no worries, you can always claim your discount once your product support has been purchased. Whether tomorrow or 5 months down the line.\n")
                        user_email_consent = input("What is the best email address to reach you in order to send your preventative guide and further resources: ")
                        print(user_email_consent)
                    else:
                        print("Oops thats not a valid option, try again. Press: A , or B \n")
                        continue      
                except:
                    error = sys.exc_info()
                    print(error[0:9])
                    print("Looks like something went wrong.. one sec!")

                try:
                    print("\n\nUser Answer: ", user_provider_consent_key[user_provider_consent])
                    print("\n-------------------------------------------------------------------------------------")
                except KeyError:
                    print("Program Exit Successful")
                    sys.exit()   
                break
    provider_or_product()#function call

    def perfect_product(): #this function provides the optimal DME(back brace) for the user whether or not user wants to see a certified provider
        print("\nGiven your assesment and symptionms - dealing with [%s] pain, [%s ]..." %(user_bp_sensations_key[user_bp_sensations],user_backpain_frequency_key[user_backpain_frequency]))
        
        if user_bp_sensations_key[user_bp_sensations] == "Sharp, stabbing, tingling, or numbness" or user_bp_sensations_key[user_bp_sensations] == " mild-ache or throb":
            print ("\n.\n.\n.\nEASY DME - recommends [insert product x- severe lumbar support product]")
            print(input("\n\nPress Enter to purchase you DME:..."))
            print("\n-------------------------------------------------------------------------------------")
            print("AWESOME!! - Your product is on the way. In the meantime check your email for a Guide to back treatment - Here's how to get your back fit again..\n\n")
        elif user_bp_sensations_key[user_bp_sensations] == "mild-ache or throb" or user_bp_sensations_key[user_bp_sensations] == "Slight-ache" or user_bp_sensations_key[user_bp_sensations] == "N/A":
            print("\n.\n.\n.\nEASY DME - recommends [insert product x- moderate lumbar support product]")
            print(input("\n\nPress Enter to purchase you DME:..."))
            print("\n-------------------------------------------------------------------------------------")
            print("AWESOME!! - Your product is on the way. In the meantime check your email for best prevention tips - for a strong back..\n\n")

    perfect_product()#function call

    #goodbye message
    print("\n-------------------------------------------------------------------------------------\n.\n.\n.\n.\n")
    print("THANK YOU FOR USING EASY DME, WE HOPE THE PROCESS WAS INFORMATIVE - Keep an eye out for helpful resources and tools from EASY DME via email\n")
    print(input("GOOOOOOOOOOOOOODIE BYEEE! - Rember, HEALTH is for LIFE\nPRESS ENTER TO EXIT PROGRAM----->"))
    

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
