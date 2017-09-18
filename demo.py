import datetime
the file is now

class BloodDonors:
    user_details = []
    messages = []
    base_message = """Dear Donors  there is Request for ,
                    Blood group:{blood_group}
                    Patient Name: {Patinet_name}
                    Address of Hospital:{address}
                    Contact:{contact}
                    Thank you for being a part of saving life !!!
                """

    def add_user(self, name, address, blood_group, contact):
        name = name[0].upper() + name[1:].lower()
        address = address[0].upper() + address[1:].lower()
        detail = {
            "name": name,
            "blood_group": blood_group,
            "address": address,
            "contact": contact,
        }
        today = datetime.date.today()
        date_text = '{today.year}/{today.month}/{today.day}'.format(
            today=today)
        detail['date'] = date_text
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_message(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                Patient_name = detail['Patient_name']
                blood_group = detail['blood_group']
                date = detail['date']
                address = detail['address']
                contact = detail['contact']
                message = self.base_message
                new_msg = message.format(
                    Patient_name=Patient_name,
                    blood_group=blood_group,
                    address=address,
                    contact=contact,
                    date=date
                )
                self.messages.append(new_msg)
            return self.messages
        return[]


obj = BloodDonors()
obj.add_user('justin', 'Thapathali', "AB+", "9843610435")
obj.add_user('shari', 'Kathmandu', "O+", "984361068")
obj.add_user('shAkKh', 'Nepal', "AB-", "79734007034")
'''
obj.add_user('shail', "A-")
obj.add_user('shakya', "AB+")
obj.get_details()
obj.make_message()
'''
