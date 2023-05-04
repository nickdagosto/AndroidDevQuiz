import random

study_guide = {
    'Chapter 2': [
        {
            'question': 'What unit of measurement should be used for font sizes in Android programming?',
            'options': [
                'a) px',
                'b) dp',
                'c) sp',
                'd) pt'
            ],
            'answer': 'C'
        }
    ],
    'Chapter 3': [
        {
            'question': 'Which of the following is NOT part of the Android Activity Lifecycle?',
            'options': [
                'a) onCreate',
                'b) onStart',
                'c) onResume',
                'd) onAttach'
            ],
            'answer': 'D'
        }
    ],
    'Chapter 4': [
        {
            'question': 'What is the purpose of ViewModel in Android programming?',
            'options': [
                'a) To store UI-related data',
                'b) To manage database connections',
                'c) To handle network requests',
                'd) To manage app permissions'
            ],
            'answer': 'A'
        },

        {
            'question': 'How does a ViewModel help mitigate memory leaks in Android app development?',
            'options': [
                'a) By using weak references for UI components',
                'b) By separating UI-related data from the Activity or Fragment lifecycle',
                'c) By using a garbage collection mechanism for network requests',
                'd) By incorporating a built-in mechanism to manage app permissions'
            ],
            'answer': 'B'
        }
    ],
    'Chapter 7': [
        {
            'question': 'Which of the following is an example of an Implicit Intent in Android programming?',
            'options': [
                'a) Opening a specific app\'s settings',
                'b) Displaying a web page in a browser',
                'c) Navigating between activities in the same app',
                'd) Displaying a list of installed apps'
            ],
            'answer': 'B'
        },
      {
            'question': 'In the context of Android app development, which of the following best describes an intent?',
            'options': [
            'a) A mechanism for opening a specific app\'s settings',
            'b) A method for displaying a web page in a browser',
            'c) A messaging object used for requesting an action from another component or the OS',
            'd) An API for displaying a list of installed apps'
            ],
            'answer': 'C'
            }
    ],
    'Chapter 10': [
        {
            'question': 'In a RecyclerView Adapter, which method is responsible for creating a ViewHolder instance?',
            'options': [
                'a) onCreateViewHolder',
                'b) onBindViewHolder',
                'c) getItemCount',
                'd) getItemViewType'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 11': [
        {
            'question': 'In a ConstraintLayout, what is the purpose of using "match_constraints"?',
            'options': [
                'a) To match the size of the parent view',
                'b) To make the view as big as its contents',
                'c) To make the view a fixed size',
                'd) To make the view expand to fill available space'
            ],
            'answer': 'D'
        }
    ],
    'Chapter 12': [
        {
            'question': 'Which of the following is NOT a part of creating a database with Room in Android programming?',
            'options': [
                'a) Defining entities',
                'b) Creating a DAO',
            'c) Implementing a Repository pattern',
            'd) Registering the database with the AndroidManifest.xml'
        ],
        'answer': 'D'
    }
],
'Chapter 13': [
    {
        'question': 'In Android navigation, what does "safeArgs" refer to?',
        'options': [
            'a) Type-safe arguments passed between navigation destinations',
            'b) A set of predefined arguments for common navigation scenarios',
            'c) A mechanism for validating navigation arguments at runtime',
            'd) A tool for generating navigation-related code'
        ],
        'answer': 'A'
    }
],
'Chapter 14': [
    {
        'question': 'What is the purpose of a DialogFragment in Android programming?',
        'options': [
            'a) To display a floating window with content',
            'b) To create reusable UI components',
            'c) To manage app settings and preferences',
            'd) To implement navigation between app screens'
        ],
        'answer': 'A'
    }
],
'Chapter 20': [
    {
        'question': 'Which of the following libraries is used for JSON parsing in Android programming?',
        'options': [
            'a) Retrofit',
            'b) Moshi',
            'c) Coil',
            'd) Glide'
        ],
        'answer': 'B'
    }
],
'Chapter 21': [
    {
        'question': 'In Android programming, what is the primary purpose of a SearchView?',
        'options': [
            'a) To display search results',
            'b) To provide a user interface for entering search queries',
            'c) To perform search queries on a data set',
            'd) To store search history'
        ],
        'answer': 'B'
    }
],
'Chapter 24': [
    {
        'question': 'In Android custom views, what is the purpose of the onDraw() method?',
        'options': [
            'a) To respond to touch events',
            'b) To create the view\'s layout',
            'c) To draw the view\'s content',
            'd) To measure the view\'s dimensions'
        ],
        'answer': 'C'
    }
],
'Chapter 25': [
    {
        'question': 'Which of the following Android components is used to play multiple animations together?',
        'options': [
            'a) AnimatorSet',
            'b) ObjectAnimator',
            'c) ValueAnimator',
            'd) AnimationDrawable'
        ],
        'answer': 'A'
    }
],
'Chapter 1': [
    {
        'question':'Q19: What is the purpose of the \'lateinit\' keyword in Kotlin?',
            'options': [
                'a) To declare a non-null variable without initializing it immediately',
                'b) To initialize a variable with a default value',
                'c) To create a singleton instance of a class',
                'd) To delay the initialization of a variable until it is first accessed'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 3': [
        {
            'question': 'Q20: In the Android Activity Lifecycle, what method is called when the activity is partially obscured by another activity?',
            'options': [
                'a) onPause',
                'b) onStop',
                'c) onDestroy',
                'd) onRestart'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 4': [
        {
            'question': 'Q21: Which of the following can cause a memory leak in Android programming?',
            'options': [
                'a) Static references to activity instances',
                'b) ViewModel instances',
                'c) SavedStateHandle instances',
                'd) Android property delegates'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 7': [
        {
            'question': 'Q22: What is the primary purpose of the AndroidManifest.xml file?',
            'options': [
                'a) To define the app\'s user interface',
                'b) To declare app components and permissions',
                'c) To store app configuration settings',
                'd) To manage the app\'s dependencies'
            ],
            'answer': 'B'
        }
    ],
    'Chapter 9': [
        {
            'question': 'Q23: What is the primary difference between Fragments and Activities in Android programming?',
            'options': [
                'a) Fragments are reusable UI components, while Activities represent app screens',
                'b) Activities are reusable UI components, while Fragments represent app screens',
                'c) Fragments are part of the Activity Lifecycle, while Activities are not',
                'd) Activities are part of the Fragment Lifecycle, while Fragments are not'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 10': [
        {
            'question': 'Q24: What is the primary responsibility of a ViewHolder in RecyclerView?',
            'options': [
                'a) To manage database connections',
                'b) To handle network requests',
                'c) To store and recycle views for efficient scrolling',
                'd) To handle app permissions'
            ],
            'answer': 'C'
        }
    ],
    'Chapter 11': [
        {
            'question': 'Q25: What is the difference between margins and padding in Android layouts?',
            'options': [
                'a) Margins define the space outside the view, while padding defines the space inside the view',
                'b) Padding defines the space outside the view, while margins define the space inside the view',
                'c) Margins and padding are interchangeable terms',
                'd) Margins define the space between views, while padding defines the space between the view\'s content and its boundaries'
            ],
            'answer': 'A'
        }
    ],
    'Chapter 12': [
        {
            'question': 'Q26: What is the primary purpose of using coroutines in Android programming?',
            'options': [
                'a) To manage app permissions',
                'b) To handle asynchronous code execution',
                'c) To store UI-related data',
                'd) To manage database connections'
            ],
            'answer': 'B'
        }
      ],
'Chapter 13': [
    {
        'question': 'Q27: What does "Unidirectional Data Flow" mean in the context of Android programming?',
        'options': [
            'a) Data flows in a single direction from a source to a destination',
            'b) Data flows in multiple directions between sources and destinations',
            'c) Data flows in a loop between sources and destinations',
            'd) Data flows in a hierarchical structure between sources and destinations'
        ],
        'answer': 'A'
    }
],
'Chapter 14': [
    {
        'question': 'Q28: What is the purpose of serialization in Android programming?',
        'options': [
            'a) To convert an object into a format suitable for storage or transmission',
            'b) To create a deep copy of an object',
            'c) To compare two objects for equality',
            'd) To manage the memory allocated for an object'
        ],
        'answer': 'A'
    }
],
'Chapter 15': [
    {
        'question': 'Q29: Which of the following is a characteristic of an overflow menu in Android programming?',
        'options': [
            'a) Appears on the app bar',
            'b) Displays a list of all available actions',
            'c) Can be accessed by pressing the three little dots',
            'd) all of the above'
        ],
        'answer': 'D'
    }
],
'Chapter 16': [
    {
        'question': 'Q30: Which of the following is NOT part of an Implicit Intent in Android programming?',
        'options': [
            'a) Action',
            'b) Data',
            'c) Category',
            'd) Component name'
        ],
        'answer': 'D'
    }
],



    'Chapter 1: GeoQuiz': [
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
            'question': 'In ConstraintLayout, what does the "match_parent" option do?',
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
    total_questions = sum(len(questions) for questions in study_guide.values())

    chapters = list(study_guide.keys())
    remaining_questions = {chapter: set(range(len(study_guide[chapter]))) for chapter in chapters}

    try:
        while sum(len(questions) for questions in remaining_questions.values()) > 0:
            chapter = random.choice(chapters)
            if not remaining_questions[chapter]:
                chapters.remove(chapter)
                continue

            question_index = random.choice(list(remaining_questions[chapter]))
            remaining_questions[chapter].remove(question_index)
            question = study_guide[chapter][question_index]

            print(f"{chapter}: {question['question']}\n")
            for option in question['options']:
                print(option)

            user_answer = input("\nEnter your answer (A/B/C/D) or 'Q' to quit: ").upper()

            if user_answer == 'Q':
                raise KeyboardInterrupt

            if user_answer == question['answer']:
                correct_answers += 1
                print("\nCorrect!\n")
            else:
                print(f"\nIncorrect. The correct answer is {question['answer']}\n")

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
