import module_student

def main():
    #create instances of each student type
    used_undergraduate = module_student.Undergraduate('Fatimah', '18DKM24F1011', 23, 'Mathematics', 2)
    used_postgraduate = module_student.Postgraduate('Hamzah', '18DIT24F1001', 20, 'Software Development', 3, 'Network Security')
    used_parttime = module_student.PartTime_Student('Zahirah', '18DHF24F1009', 19, 'Halal Food', 2, 'Sains Halal', 12)

    #display student information
    print('Student Name:', used_undergraduate.get_name())
    print('Student Id:', used_undergraduate.get_id())
    print('Student Age:', used_undergraduate.get_age())
    print('Student Course:', used_undergraduate.get_course())
    print('Student Year Level:', used_undergraduate.get_year())
    print()

    print('Student Name:', used_postgraduate.get_name())
    print('Student Id:', used_postgraduate.get_id())
    print('Student Age:', used_postgraduate.get_age())
    print('Student Course:', used_postgraduate.get_course())
    print('Student Year Level:', used_postgraduate.get_year())
    print('Student Research Topic:', used_postgraduate.get_topic())
    print()

    print('Student Name:', used_parttime.get_name())
    print('Student Id:', used_parttime.get_id())
    print('Student Age:', used_parttime.get_age())
    print('Student Course:', used_parttime.get_course())
    print('Student Year Level:', used_parttime.get_year())
    print('Student Research Topic:', used_parttime.get_topic())
    print('Student Work Hours:', used_parttime.get_workhour())
    print()

main()