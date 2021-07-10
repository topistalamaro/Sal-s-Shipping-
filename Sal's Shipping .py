#!/usr/bin/env python
# coding: utf-8

# ## Sal's Shipping 

# In[2]:


weight = 4.8

#Ground Shipping

if weight <= 2:
  ground_cost = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
  ground_cost = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
  ground_cost = weight * 4.00 + 20.00
else:
  ground_cost = weight * 4.75 + 20.00

print('Ground Shipping: $ ' + str(ground_cost))

#Ground Shipping Premium
groud_cost_premium = 125.00
print('Ground Shipping Premimium: $ ' + str(groud_cost_premium))

#Drone Shipping 
if weight <= 2:
  ground_cost_drone = weight * 4.50 
elif weight > 2 and weight <= 6:
   ground_cost_drone = weight * 9.00 
elif weight > 6 and weight <= 10:
   ground_cost_drone = weight * 12.00 
else:
   ground_cost_drone = weight * 14.25 

print('Drone Shipping: $ ' + str(ground_cost_drone))



# In[ ]:




