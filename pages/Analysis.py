import streamlit as st
#Some analysis
st.header('Some Analysis about the dataset')
st.write('we chose a real dataset about hotel demand in order to help hotels operate and manage better. (The dataset we chose is three years old, avoiding the impact of the new crown).After getting the data, our first step was to process the missing data, and the second step was to remove some of the duplicate data to ensure the accuracy of the analysis. The third step we then used box-plot and hist for the overall data analysis, replacing outliers with the closest maximum or minimum values')
#question1
st.subheader('Question1: How do hotel cancellation rate trends change?')
st.markdown('![cancellation about year and month](https://user-images.githubusercontent.com/115609247/200618738-608467c6-0086-4dbf-a4ce-db9c1a84f4cc.jpg)')
st.write(' In terms of months, actually, the overall rate of change for hotels does not fluctuate very much. It is mainly in July and August that the cancellation rate is slightly higher due to the number of holidays booked, and it is still fluctuating at 20%-30% by and large. But the cancellation rate in these years is increasing year by year. We think this is an issue worthy of the hotel\'s attention, which determines the hotel\'s business situation in the later years.')

#question2
st.subheader('Question2: What factors influence its cancellation rate?')
#Factor1
st.subheader('Factor1: Deposit')
st.markdown('![deposite 2](https://user-images.githubusercontent.com/115609247/200618788-28914429-868d-4a64-b9af-5343e8776a81.jpg)')
st.write('From this chart, we can see that the number of customers who cancel the reservation without paying the deposit is far greater than other kinds. Through the analysis, the reason is that when they don’t pay the deposit, they do not care about the reservation and cancel it  if they want.')

#Factor2
st.subheader('Factor2: Advanced booking time and children')
st.markdown('![adanced booking time and children ](https://user-images.githubusercontent.com/115609247/200618795-e9023330-4f68-430b-8a68-ed4c79c18518.jpg)')

col1,col2=st.columns(2)
col1.write('The second factor is related to the time of booking in advance and whether the adults have children.let’s focus on the two pictures. Both pictures show the increase in the cancellation rate as the advanced time goes longer. It is obvious that the longer the schedule is in advance, the more variables will appear during the long period, and the cancellation will be high. ')
col2.write('Now let\'s look at the comparison of the two pictures below. In the first picture, only adults go to the hotel, the fluctuated range is about 15 percent. And in the second picture, when adults and children booking the hotel. the range was about 35 percentThis also shows that when a family travels with their children, there will often be more uncertainties and a higher cancellation rate.')

#Factor3
st.subheader('Factor3: Different customer type')
st.markdown('![customer type](https://user-images.githubusercontent.com/115609247/200618804-9f12c489-b3cb-4fc1-b858-32e257f10b62.jpg)')
st.write('Let\'s look at the first graph. The orange and red lines represent contrast and groups, respectively, they both show large fluctuations, while the blue and green lines are basically flat. Because the group or contrast always contains huge people,  if the tourism cancel it, it will leads so many room be cancelled.')
st.write('When we talk about how these customers book from different channels, we\'ll find something new. By comparing the two figures above and below, we can see that the cancellation rate of customers who book online is higher than that of customers who book directly, which is related to people\'s impulse consumption on the Internet.')
st.write('When we look at the second picture, we will find a strange line, which is the contract, it starts in August and end in October. We investigated the dataset again in detail and found that in other months, the data did not exist, but in August to October, only one data met the requirement, so there was a 100% cancellation rate and a 0% cancellation rate. Therefore, whether this data has reference value is still worth further exploration.')


st.caption('This is our project,Thanks!')
