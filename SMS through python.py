#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install vonage


# In[3]:


import vonage
client = vonage.Client(key="7f839cc0", secret="ieEz4uYD4kSfV7GP")
sms = vonage.Sms(client)


# In[6]:


responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": input ("enter the reciever number"),
        "text": input ("enter the message"),
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")


# In[ ]:




