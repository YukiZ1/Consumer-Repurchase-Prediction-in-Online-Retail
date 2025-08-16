The prediction of repurchase problem is a classic marketing problem. At present, the competition among online retailers is fierce. According to the network data, the collapse rate of Taobao stores in 2018 is as high as 85%. 
How to increase users' purchase is particularly important to ensure their survival. Due to the recommendation and drainage mechanism of e-commerce platform, the cost of retaining old customers is far lower than developing new customers. 
**How to use online shopping data to predict whether users will buy again has become the key to online store revenue.** However, some studies still focus on the questionnaire survey data to analyze the subjective factors of re purchase, 
while the feature engineering in big data analysis is not comprehensive enough and fails to explain the influence principle behind the features. 

Therefore, this paper focuses on Feature Engineering. Firstly, **literature review** is carried out to sort out the existing research on influencing factors and prediction of repurchase. 
Then, we build a **consumer repurchase prediction model** with 25 characteristics including four aspects: **user based feature group, commodity based feature group, commodity promotion feature group and user behavior feature group**. 
And use the purchase data of Jingdong to carry out empirical analysis to verify the model. 

Four binary classifiers—XGBoost, Random Forest, Logistic Regression, and SVM—were employed for training and prediction.
Model performance was evaluated using Monte Carlo Cross-Validation with uniform random sampling. XGBoost achieved the best performance, with consistently high accuracy and AUC across trials and notably shorter runtime.
<img width="641" height="187" alt="image" src="https://github.com/user-attachments/assets/ea5d58d7-4aef-47e6-906a-3f8af5d8be15" />

The important characteristics of each group are the month of first purchase, the brand of the product, the final price of the product in the order, and the total number of clicks before placing the order. 
<img width="650"  alt="image" src="https://github.com/user-attachments/assets/f79b6807-7699-4ae3-a520-06465c0fee69" />

In addition, experiments with different feature groups verify both the importance and irreplaceability of each feature group. 
The results show that **product features**, despite a lower standalone AUC (0.6615), **provide unique and irreplaceable information for prediction**, as indicated by the lowest exclusive AUC (0.7521). 
**Promotion features** yield the **highest standalone AUC** (0.7253), indicating their strong predictive power; But their high exclusive AUC (0.7554) suggests redundancy in order-related information. 
In contrast, **user behavior features** **contribute little additional value**, since their standalone AUC (0.6486) is the lowest and their exclusive AUC (0.7692) is nearly identical to that of the full-feature model.

Finally, according to the characteristic analysis, we give some **suggestions to promote re-purchase**. 
**For retailers**, focus on brand building to attract repeat customers and target users based on their first-purchase timing to retain loyalty. 
**For e-commerce platforms**, encourage merchant participation in discounts, highlight key promotional information (final price, total discount, product-specific discounts), and repeatedly display frequently clicked products to stimulate repurchase.

KEY WORDS：**rebuy prediction  feature engineering  E-commerce**
