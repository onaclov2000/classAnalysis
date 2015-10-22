from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
   
def full(a):
    return not a[13] == '0'
def wait(a):
    return not a[16] == '0'

def print_classes(a, b):
    registerable_classes = filter(full, a)
    waitlist_classes = filter(wait, a)

    print "Classes you can register for NOW in your degree"
    for omscs in registerable_classes:
        for cl in b:
             if cl in omscs:
                print omscs

    print "Classes you can get on a waitlist for"
    for omscs in waitlist_classes:
        for cl in b:
             if cl in omscs:
                print omscs
                

    # print 'All classes offered this semester'
    # for omscs in a:
        # print omscs
        
        
        
f = open('./BuzzPort_files/login.htm')
list = []
for line in f:
    if 'td class="dddefault"' in line:
    
    # <td class="dddefault"><abbr title="Not available for registration">NR</abbr></td>
# <td class="dddefault"><a href="https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_listcrse?term_in=201602&amp;subj_in=CS&amp;crse_in=1100&amp;crn_in=28961" onmouseover="window.status='Detail';  return true" onfocus="window.status='Detail';  return true" onmouseout="window.status='';  return true" onblur="window.status='';  return true">28961</a></td>
# <td class="dddefault">CS</td>
# <td class="dddefault">1100</td>
# <td class="dddefault">A</td>
# <td class="dddefault">A</td>
# <td class="dddefault">P</td>
# <td class="dddefault">1.0</td>
# <td class="dddefault">Freshman Leap Seminar</td>
# <td class="dddefault">W</td>
# <td class="dddefault">09:05 am-09:55 am</td>
# <td class="dddefault">100</td>
# <td class="dddefault">0</td>
# <td class="dddefault">100</td>
# <td class="dddefault">0</td>
# <td class="dddefault">0</td>
# <td class="dddefault">0</td>
# <td class="dddefault">Raczynski, K. (<abbr title="Primary">P</abbr>)</td>
# <td class="dddefault">Klaus 2443</td>
# <td class="dddefault">&nbsp;</td>

       list.append(strip_tags(line.strip()[22:-5]))

a_class = []
for i in range(len(list)):
    if 'NR' in list[i]:
        if 'O01' in list[i+4]:
            #print list[i+4]
            a_class.append(list[i:i+20])

computational_perception_robotics ={'8803-O01' : 'Artificial Intelligence for Robotics', '7495' : 'Computer Vision', '6475': 'Computational Photography', '7641' : 'Machine Learning', '6601': 'Artificial Intelligence', '6505': 'ComputabilityAlgorithms'}
computing_systems ={'6505': 'ComputabilityAlgorithms', '6210': 'Advanced Operating Systems', '6250': 'Computer Networks', '6290': 'High-Performance Computer Architecture', '6300' :'Software Development Process', '6400' : 'Database Systems Concepts and Design', '6035' : 'Introduction to Information Security', '6262' : 'Network Security', '6310': 'Software Architecture and Design'}
high_performance_computing = {'6220' : 'Intro to High Performance Computing', '6290': 'High-Performance Computer Architecture'}
interactive_intelligence = {'6300' : 'Software Development Process', '6505': 'ComputabilityAlgorithms', '6601': 'Artificial Intelligence', '7637' : 'Knowledge-Based AI', '7641' : 'Machine Learning', '6440' : 'Introduction to Health Informatics', '6460' : 'Educational Technology: Conceptual Foundations'}
machine_learning = {'6505': 'ComputabilityAlgorithms', '7641' : 'Machine Learning', '7646':'Mach Learn For Trading'}


classes_ive_taken = ['7641']
wanted_classes = ['Intro Health Informatics', 'Software Arch  Design', 'Machine Learning']

computational_perception_robotics_left = set(computational_perception_robotics.keys()) - set(classes_ive_taken)
computer_systems_left = set(computing_systems.keys()) - set(classes_ive_taken)
high_performance_computing_left = set(high_performance_computing.keys()) - set(classes_ive_taken)
interactive_intelligence_left = set(interactive_intelligence.keys()) - set(classes_ive_taken)
machine_learning_left = set(machine_learning.keys()) - set(classes_ive_taken)

print 'Computational Perception Robotics'
print_classes(a_class, computational_perception_robotics.keys())


print 'Computer Systems'
print_classes(a_class, computing_systems.keys())

print 'High Performance Computing'
print_classes(a_class, high_performance_computing.keys())

print 'Interactive Intelligence'
print_classes(a_class, interactive_intelligence.keys())

print 'Machine Learning'
print_classes(a_class, machine_learning.keys())
   
