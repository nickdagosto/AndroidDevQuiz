import random

study_guide = {
    'Chapter 1: GeoQuiz': [
        {
            'question': 'Which of the following is NOT a concept covered in Chapter 1 of GeoQuiz?',
            'options': [
                'a) Activity',
                'b) ReverseDNS',
                'c) lateinit',
                'd) RecyclerView'
            ],
            'answer': 'C'
        },
        {
            'question': 'What is the purpose of the "Toast" class in Android development?',
            'options': [
                'a) Displaying notifications or short messages to the user',
                'b) Handling activity lifecycle events',
                'c) Wiring up views in a layout',
                'd) Creating layouts using XML'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 2: GeoQuiz': [
        {
            'question': 'How does wiring up views work using ViewBinding?',
            'options': [
                'a) It automatically generates code for accessing views in a layout',
                'b) Views are manually instantiated and connected to layout XML files',
                'c) ViewBinding is not used for wiring up views',
                'd) Views are wired up using the "Toast" class'
            ],
            'answer': 'A'
        },
        {
            'question': 'Which unit of measurement is commonly used for specifying text size in Android?',
            'options': [
                'a) ps',
                'b) dp',
                'c) sp',
                'd) in'
            ],
            'answer': 'C'
        }
    ],
    'Chapter 3: GeoQuiz': [
        {
            'question': 'What does Figure 3.3 in Chapter 3 of GeoQuiz illustrate?',
            'options': [
                'a) The layout structure of an activity',
                'b) The activity lifecycle states',
                'c) The wiring up process using ViewBinding',
                'd) The use of "lateinit" in Kotlin'
            ],
            'answer': 'B'
        },
        {
            'question': 'How can log functions be used to monitor the activity lifecycle?',
            'options': [
                'a) By displaying toast messages',
                'b) By printing log messages to the logcat',
                'c) By changing the layout of the activity dynamically',
                'd) By triggering explicit intents'
            ],
            'answer': 'B'
        }
    ],
    'Chapter 4: GeoQuiz': [
        {
            'question': 'Which component is responsible for managing the lifecycle of a ViewModel?',
            'options': [
                'a) Activity',
                'b) SavedStateHandle',
                'c) ViewModel lifecycle',
                'd) Fragment'
            ],
            'answer': 'C'
        },
        {
            'question': 'What is a potential issue associated with improper handling of ViewModel instances?',
            'options': [
                'a) Memory leak',
                'b) ReverseDNS lookup failure',
                'c) Incompatible layout design',
                'd) Invalid R class reference'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 7: GeoQuiz': [
        {
            'question': 'Which file is used to declare activities in the AndroidManifest.xml file?',
            'options': [
                'a) R class',
                'b) Toast class',
                'c) ActivityManager',
                'd) Manifest file'
            ],
            'answer': 'D'
        },
        {
            'question': 'How can an activity start another activity using an explicit intent?',
            'options': [
                'a) By calling the `startActivity(Intent)` method',
                'b) By using theContext` class',
                'c) By using the Intent Extras',
                'd) By defining a companion object'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 9: CriminalIntent': [
        {
            'question': 'What is the primary difference between fragments and activities?',
            'options': [
                'a) Fragments cannot be added dynamically at runtime',
                'b) Fragments do not have their own lifecycle',
                'c) Activities are used for UI components, while fragments are used for non-UI tasks',
                'd) Activities are tied to a specific screen, while fragments can be reused in multiple screens'
            ],
            'answer': 'D'
        },
        {
            'question': 'How can data binding between a fragment and its layout be achieved?',
            'options': [
                'a) Using the FragmentManager',
                'b) By implementing the back binding technique',
                'c) Fragments do not support data binding',
                'd) By using the Adapter class'
            ],
            'answer': 'C'
        }
    ],
    'Chapter 10: CriminalIntent': [
        {
            'question': 'What is the purpose of RecyclerView in Android development?',
            'options': [
                'a) It is used for managing the lifecycle of fragments',
                'b) It provides a way to display a scrollable list of items efficiently',
                'c) RecyclerView is used for data serialization',
                'd) It is responsible for handling explicit intents'
            ],
            'answer': 'B'
        },
        {
            'question': 'Which method(s) must be overridden when creating a custom adapter for RecyclerView?',
            'options': [
                'a) onCreateViewHolder()',
                'b) onBindViewHolder()',
                'c) getItemCount()',
                'd) All of the above'
            ],
            'answer': 'D'
        }
    ],
    'Chapter 11: CriminalIntent': [
        {
            'question': 'In ConstraintLayout, what does the "match constraints" option do?',
            'options': [
                'a) It makes the view\'s size match the size of its parent layout',
                'b) It sets the view\'s size to a fixed value in pixels',
                'c) It adjusts the view\'s size based on its content',
                'd) None of the above'
            ],
            'answer': 'A'
        },
        {
            'question': 'What is the difference between margins and padding in Android layouts?',
            'options': [
                'a) Margins define the space outside the view, while padding defines the space inside the view',
                'b) Margins define the space inside the view, while padding defines the space outside the view',
                'c) Margins and padding are interchangeable terms in Android layouts',
                'd) Margins and padding have the same effect on the layout'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 12: CriminalIntent': [
        {
            'question': 'What is a coroutine in Kotlin?',
            'options': [
                'a) A design pattern for managing database operations',
                'b) A type of animation used for visual effects',
                'c) A lightweight thread-like structure for asynchronous programming',
                'd) A method for defining entity classes in Room'
            ],
            'answer': 'C'
        },
        {
            'question': 'Which step is NOT part of creating a database with Room?',
            'options': [
                'a) Defining entities',
                'b) Implementing type converters',
                'c) Defining a DAO (Data Access Object)',
                'd) Initializing singleton Application classes'
            ],
            'answer': 'D'
        }
    ],
    'Chapter 13: CriminalIntent': [
        {
            'question': 'How can fragment navigation be performed in Android?',
            'options': [
                'a) By calling the `findNavController().navigate()` method',
                'b) By using the Intent class',
                'c) By using the GlobalScope',
                'd) By registering for activity results with `ActivityResultContracts.StartActivityForResult`'
            ],
            'answer': 'A'
        },
        {
            'question': 'What are safeArgs in Android navigation?',
            'options': [
                'a) Arguments that can be passed between fragments safely',
                'b) Special permissions required for fragment transactions',
                'c) A type of interpolator used for animations',
                'd) The navigation graph file for fragment navigation'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 14: CriminalIntent': [
        {
            'question': 'What is a DialogFragment in Android?',
            'options': [
                'a) A fragment used for handling HTTP requests',
                'b) A fragment specifically designed for displaying dialogs',
                'c) A class for handling date and time calculations',
                'd) A fragment responsible for managing image galleries'
            ],
            'answer': 'B'
        },
        {
            'question': 'Which class can be used for handling dates and times in Java and Android?',
            'options': [
                'a) GregorianCalendar',
                'b) Retrofit',
                'c) ViewModel',
                'd) RecyclerView'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 15: CriminalIntent': [
        {
            'question': 'What is the purpose of an app bar in Android?',
            'options': [
                'a) It provides a space for displaying application-specific actions or menus',
                'b) It manages the layout of fragments in the activity',
                'c) It defines the overall theme and style of the application',
                'd) It handles the back navigation within the app'
            ],
            'answer': 'A'
        },
        {
            'question': 'Which attribute is used to specify the behavior of menu items in the app bar?',
            'options': [
                'a) ifRoom',
                'b) withText',
                'c) overflow menu',
                'd) All of the above'
            ],
            'answer': 'D'
        }
    ],
    'Chapter 16: CriminalIntent': [
        {
            'question': 'What are implicit intents in Android?',
            'options': [
                'a) Intents that are declared in the manifest file',
                'b) Intents that are created and explicitly defined in code',
                'c) Intents that are used for inter-process communication',
                'd) Intents that do not specify a particular component to start'
            ],
            'answer': 'D'
        },
        {
            'question': 'What is data migration in the context of Android development?',
            'options': [
                'a) The process of transferring data between databases',
                'b) The process of updating an app\'s data format or structure',
                'c) The process of encrypting sensitive data',
                'd) The process of compressing data for storage optimization'
            ],
            'answer': 'B'
        }
    ],
    'Chapter 20: PhotoGallery': [
        {
            'question': 'What is Retrofit used for in Android development?',
            'options': [
                'a) Handling network requests and REST API communication',
                'b) Parsing JSON data',
                'c) Managing database operations with Room',
                'd) Displaying images with Coil library'
            ],
            'answer': 'A'
        },
        {
            'question': 'Which library is commonly used for parsing JSON in Android?',
            'options': [
                'a) Moshi',
                'b) Retrofit',
                'c) Coil',
                'd) DataStore'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 21: PhotoGallery': [
        {
            'question': 'What is an Interceptor in the context of network requests?',
            'options': [
                'a) A mechanism for handling permission requests',
                'b) A class responsible for intercepting and modifying network requests and responses',
                'c) An Android component used for navigation between fragments',
                'd) A design pattern for managing database operations'
            ],
            'answer': 'B'
        },
        {
            'question': 'What is DataStore in Android?',
            'options': [
                'a) A library for handling image loading and caching',
                'b) A storage solution for app-specific key-value data',
                'c) A utility class for creating animations',
                'd) An architecture component for managing UI-related data'
            ],
            'answer': 'B'
        }
    ],
    'Chapter 24: One-Shot': [
        {
            'question': 'Which method is commonly overridden to handle touch events in a custom View?',
            'options': [
                'a) onTouchEvent()',
                'b) onDraw()',
                'c) invalidate()',
                'd) requestLayout()'
            ],
            'answer': 'A'
        },
        {
            'question': 'What does the "invalidate()" method do in Android?',
            'options': [
                'a) Invalidates the current layout and triggers a redraw',
                'b) Invalidates the current View object and releases system resources',
                'c) Invalidates the current data in a database',
                'd) Invalidates the current thread and restarts its execution'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 25: One-Shot': [
        {
            'question': 'What is ObjectAnimator used for in Android animations?',
            'options': [
                'a) Playing audio files',
                'b) Animating object properties, such as position or size',
                'c) Creating custom interpolators',
                'd) Loading and caching images from the network'
            ],
            'answer': 'B'
        },
        {
            'question': 'What is the purpose of the "by lazy" syntax in Kotlin?',
            'options': [
                'a) It declares a lazy property that is initialized only when accessed for the first time',
                'b) It specifies the duration of an animation',
                'c) It defines a custom interpolator for animations',
                'd) It creates a new instance of a class using the Builder pattern'
            ],
            'answer': 'A'
        }
    ]
}

            


def main():
    print("Android Development Quiz")
    print("-------------------------")

    correct_answers = 0
    total_questions = 0

    chapters = list(study_guide.keys())
    random.shuffle(chapters)

    try:
        for chapter in chapters:
            questions = study_guide[chapter]
            random.shuffle(questions)

            for question in questions:
                print(f"{chapter}: {question['question']}")
                for option in question['options']:
                    print(option)

                user_answer = input("Enter your answer (A/B/C/D) or 'Q' to quit: ").upper()

                if user_answer == 'Q':
                    raise KeyboardInterrupt

                if user_answer == question['answer']:
                    correct_answers += 1
                    print("Correct!\n")
                else:
                    print(f"Incorrect. The correct answer is {question['answer']}\n")

                total_questions += 1

    except KeyboardInterrupt:
        pass

    finally:
        print("\nQuiz Results")
        print("------------")
        print(f"Total questions: {total_questions}")
        print(f"Correct answers: {correct_answers}")
        print(f"Score: {correct_answers / total_questions * 100}%")

if __name__ == '__main__':
    main()
