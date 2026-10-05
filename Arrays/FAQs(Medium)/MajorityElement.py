l1 = [7,0,0,1,7,7,2,7,7]

def majority_element(l1):
    m_element = 0
    count = 0
    for i in l1:
        if count == 0:
            m_element = i
            count += 1
        else:
            if i != m_element:
                count -= 1
            else:
                count += 1
    return m_element

me = majority_element(l1)

print(me)