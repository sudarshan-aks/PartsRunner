import requests
import time

# Define your dynamic variables
quantity = "20"
item_wanted = "sheets of 3/4 inch plywood"
location = "123 Job Site Lane"

voice_agent_response = requests.post(
    'https://teli-hackathon--transfer-message-service-fastapi-app.modal.run/v1/agents',
    headers={'X-API-Key': 'hackathon-sms-api-key-h4ck-2024-a1b2-c3d4e5f67890'},
    json={
        "agent_type": "voice",
        "agent_name": "Price Negotiator",
        "starting_message": f"Hi, I'm calling from PartsRunner. I'm looking for the best price on {quantity} of {item_wanted}.",
        "prompt": f"""You are a professional procurement agent for PartsRunner.
GOAL: Secure the LOWEST possible price and confirm availability for {quantity} of {item_wanted}.

CRITICAL RULES:
1. Ask only ONE question at a time. Wait for the vendor to answer before moving to the next step.
2. Do not stack questions (e.g., do not ask for price and delivery in the same sentence).
3. Do not authorize payments or give credit card info.

CONVERSATION SCRIPT(use judgement to ensure you get all details needed, and confirm once after each question to ensure you have the correct details):
Step 1 (Availability): Ask if they have {quantity} of {item_wanted} in stock right now, and if not then when they will have it available?
Step 2 (Price): Ask: "What is the absolute lowest price per unit you can offer?"
Step 3 (Tax): Ask: "Does that price include tax? If no, then ask the total cost with tax?"
Step 4 (Delivery): Ask: "Can I get this product delivered to {location}?"
Step 5 (only do this step if they said they can deliver): What is the cost for delivery?"
Step 6 (Closing): Tell them you will call back to confirm and put a hold on the product, and say goodbye.

If they do not have the item: Ask for a comparable substitute or when they expect stock.""",
        "organization_id": "1769903836421x454252683899297604",
        "user_id": "1769905924470x566126461042309713",
        "voice_id": "11labs-Adrian",
        "language": "en-US",
        "extraction_fields": [
            "unit_price",
            "total_cost",
            "delivery_available",
            "delivery_cost",
            "in_stock",
            "date_available"
        ],
        "general_tools": [
            {
                "type": "end_call",
                "name": "end_call",
                "description": "End the call when the conversation is complete, after saying goodbye in Step 6"
            }
        ]
    }
    
)

data = voice_agent_response.json()

print(data['voice_agent_id'])
print(data)



# response = contact_group.json()
# print(contact_response)
# contact = requests.post(
#     'https://teli-hackathon--transfer-message-service-fastapi-app.modal.run/v1/contacts',
#     headers={'X-API-Key': 'hackathon-sms-api-key-h4ck-2024-a1b2-c3d4e5f67890'},
#     json={
#         "organization_id": "1769903836421x454252683899297604",
#         "user_id": "1769905924470x566126461042309713",
#         "list_id": '1769913795214x123958324320183458',
#         "phone_number": "+13318145500",
#         "first_name": "John",
#         "last_name": "Doe",
#         "email": "john.doe@example.com"
#     }
# )
# contact_response = contact.json()
# print(contact_response)
# leads = requests.get(
#     'https://teli-hackathon--transfer-message-service-fastapi-app.modal.run/v1/organizations/1769903836421x454252683899297604/leads',
#     headers={'X-API-Key': 'hackathon-sms-api-key-h4ck-2024-a1b2-c3d4e5f67890'},)
# leads_response = leads.json()
# print(leads_response)
# contact_
# create_newphone = requests.post(
#     'https://teli-hackathon--transfer-message-service-fastapi-app.modal.run/v1/voice/phone-numbers/create',
#     headers={'X-API-Key': 'hackathon-sms-api-key-h4ck-2024-a1b2-c3d4e5f67890'},
#     json={
#     "area_code": "517",
#     "user_id": "1769905924470x566126461042309713",
#     "organization_id": "1769903836421x454252683899297604",
#     "tenant_id": "hackathon",
#     "nickname": "Dirky"
#     })
# newphone = create_newphone.json()
# print(newphone)
voice_campaign = requests.post(
    'https://teli-hackathon--transfer-message-service-fastapi-app.modal.run/v1/voice/campaigns',
    headers={'X-API-Key': 'hackathon-sms-api-key-h4ck-2024-a1b2-c3d4e5f67890'},
    json={"leads":
        [{"phone_number": "+13318145500"}],
        "voice_agent_id": data['voice_agent_id'],
        "agent_outbound_number": "+15172529016",
        "organization_id": "1769903836421x454252683899297604",
        "tenant_id": "hackathon",
        "user_id": "1769905924470x566126461042309713"})
# agent = requests.get(
#     f'https://teli-hackathon--transfer-message-service-fastapi-app.modal.run/v1/agents/{data['voice_agent_id']}',
#     headers={'X-API-Key': 'hackathon-sms-api-key-h4ck-2024-a1b2-c3d4e5f67890'}
# )
# agent_res = agent.json()
# print(agent_res)

# while True:
#     voice_campaign_res = voice_campaign.json() 
#     # print(voice_campaign.status_code)
#     try:
#         print(voice_campaign_res["campaign_end_time"])
#         break
#     except:
#         continue

voice_campaign_res = voice_campaign.json()
# pause_campaign = requests.post(
#     f'https://teli-hackathon--transfer-message-service-fastapi-app.modal.run/v1/voice/campaigns/{voice_campaign_res["campaign_id"]}/calls',
#     headers={'X-API-Key': 'hackathon-sms-api-key-h4ck-2024-a1b2-c3d4e5f67890'}
# )
print("before loop")
while True:
    print("during loop")
    call_id = requests.get(
    f'https://teli-hackathon--transfer-message-service-fastapi-app.modal.run/v1/voice/campaigns/{voice_campaign_res["campaign_id"]}/calls',
    headers={'X-API-Key': 'hackathon-sms-api-key-h4ck-2024-a1b2-c3d4e5f67890'},
    )
    call_id_res = call_id.json()
    if call_id_res["count"]>=3:

        voice_campaign_res = voice_campaign.json()
        break
print(voice_campaign_res["campaign_id"])

call_id = requests.get(
    f'https://teli-hackathon--transfer-message-service-fastapi-app.modal.run/v1/voice/campaigns/{voice_campaign_res["campaign_id"]}/calls',
    headers={'X-API-Key': 'hackathon-sms-api-key-h4ck-2024-a1b2-c3d4e5f67890'},
)
call_id_res = call_id.json()
print(call_id_res)

agent_list = requests.get(
    'https://teli-hackathon--transfer-message-service-fastapi-app.modal.run/v1/agents',
    headers={'X-API-Key': 'hackathon-sms-api-key-h4ck-2024-a1b2-c3d4e5f67890'},
    params = {'organization_id': "1769903836421x454252683899297604"},
)
agent_list_res = agent_list.json()
print(agent_list_res["agents"])
count = 0
for agent in agent_list_res["agents"]:
    count += 1
    print(count)

    id = (agent["agent_id"])
    delete_agents = requests.delete(f"https://teli-hackathon--transfer-message-service-fastapi-app.modal.run/v1/agents/{id}", headers = {'X-API-Key': 'hackathon-sms-api-key-h4ck-2024-a1b2-c3d4e5f67890'} )
    print("")
    print("deleted agent")