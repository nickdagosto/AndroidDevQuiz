import random

study_guide = {
  'Chapter 2': [{
    'question':
    'What unit of measurement should be used for font sizes in Android programming?',
    'options': [' px', ' dp', ' sp', ' pt'],
    'answer': 'C'
  }],
  'Chapter 3': [{
    'question':
    'Which of the following is NOT part of the Android Activity Lifecycle?',
    'options': [' onCreate', ' onStart', ' onResume', ' onAttach'],
    'answer':
    'D'
  }],
  'Chapter 4': [{
    'question':
    'What is the purpose of ViewModel in Android programming?',
    'options': [
      ' To store UI-related data', ' To manage database connections',
      ' To handle network requests', ' To manage app permissions'
    ],
    'answer':
    'A'
  }, {
    'question':
    'How does a ViewModel help mitigate memory leaks in Android app development?',
    'options': [
      ' By using weak references for UI components',
      ' By separating UI-related data from the Activity or Fragment lifecycle',
      ' By using a garbage collection mechanism for network requests',
      ' By incorporating a built-in mechanism to manage app permissions'
    ],
    'answer':
    'B'
  }],
  'Chapter 7': [{
    'question':
    'Which of the following is an example of an Implicit Intent in Android programming?',
    'options': [
      ' Opening a specific app\'s settings',
      ' Displaying a web page in a browser',
      ' Navigating between activities in the same app',
      ' Displaying a list of installed apps'
    ],
    'answer':
    'B'
  }, {
    'question':
    'In the context of Android app development, which of the following best describes an intent?',
    'options': [
      ' A mechanism for opening a specific app\'s settings',
      ' A method for displaying a web page in a browser',
      ' A messaging object used for requesting an action from another component or the OS',
      ' An API for displaying a list of installed apps'
    ],
    'answer':
    'C'
  }],
  'Chapter 10': [{
    'question':
    'In a RecyclerView Adapter, which method is responsible for creating a ViewHolder instance?',
    'options': [
      ' onCreateViewHolder', ' onBindViewHolder', ' getItemCount',
      ' getItemViewType'
    ],
    'answer':
    'A'
  }],
  'Chapter 11': [{
    'question':
    'In a ConstraintLayout, what is the purpose of using "match_constraints"?',
    'options': [
      ' To match the size of the parent view',
      ' To make the view as big as its contents',
      ' To make the view a fixed size',
      ' To make the view expand to fill available space'
    ],
    'answer':
    'D'
  }],
  'Chapter 12': [{
    'question':
    'Which of the following is NOT a part of creating a database with Room in Android programming?',
    'options': [
      ' Defining entities', ' Creating a DAO',
      ' Implementing a Repository pattern',
      ' Registering the database with the AndroidManifest.xml'
    ],
    'answer':
    'D'
  }],
  'Chapter 13': [{
    'question':
    'In Android navigation, what does "safeArgs" refer to?',
    'options': [
      ' Type-safe arguments passed between navigation destinations',
      ' A set of predefined arguments for common navigation scenarios',
      ' A mechanism for validating navigation arguments at runtime',
      ' A tool for generating navigation-related code'
    ],
    'answer':
    'A'
  }],
  'Chapter 14': [{
    'question':
    'What is the purpose of a DialogFragment in Android programming?',
    'options': [
      ' To display a floating window with content',
      ' To create reusable UI components',
      ' To manage app settings and preferences',
      ' To implement navigation between app screens'
    ],
    'answer':
    'A'
  }],
  'Chapter 20': [{
    'question':
    'Which of the following libraries is used for JSON parsing in Android programming?',
    'options': [' Retrofit', ' Moshi', ' Coil', ' Glide'],
    'answer': 'B'
  }],
  'Chapter 21': [{
    'question':
    'In Android programming, what is the primary purpose of a SearchView?',
    'options': [
      ' To display search results',
      ' To provide a user interface for entering search queries',
      ' To perform search queries on a data set',
      ' To store search history'
    ],
    'answer':
    'B'
  }],
  'Chapter 24': [{
    'question':
    'In Android custom views, what is the purpose of the onDraw() method?',
    'options': [
      ' To respond to touch events', ' To create the view\'s layout',
      ' To draw the view\'s content', ' To measure the view\'s dimensions'
    ],
    'answer':
    'C'
  }],
  'Chapter 25': [{
    'question':
    'Which of the following Android components is used to play multiple animations together?',
    'options': [
      ' AnimatorSet', ' ObjectAnimator', ' ValueAnimator',
      ' AnimationDrawable'
    ],
    'answer':
    'A'
  }],
  'Chapter 1': [{
    'question':
    'Q19: What is the purpose of the \'lateinit\' keyword in Kotlin?',
    'options': [
      ' To declare a non-null variable without initializing it immediately',
      ' To initialize a variable with a default value',
      ' To create a singleton instance of a class',
      ' To delay the initialization of a variable until it is first accessed'
    ],
    'answer':
    'A'
  }],
  'Chapter 3': [{
    'question':
    'Q20: In the Android Activity Lifecycle, what method is called when the activity is partially obscured by another activity?',
    'options': [' onPause', ' onStop', ' onDestroy', ' onRestart'],
    'answer':
    'A'
  }],
  'Chapter 4': [{
    'question':
    'Q21: Which of the following can cause a memory leak in Android programming?',
    'options': [
      ' Static references to activity instances', ' ViewModel instances',
      ' SavedStateHandle instances', ' Android property delegates'
    ],
    'answer':
    'A'
  }],
  'Chapter 7': [{
    'question':
    'Q22: What is the primary purpose of the AndroidManifest.xml file?',
    'options': [
      ' To define the app\'s user interface',
      ' To declare app components and permissions',
      ' To store app configuration settings and manage dependencies',
      ' All of the above'
    ],
    'answer':
    'D'
  }],
  'Chapter 9': [{
    'question':
    'Q23: What is the primary difference between Fragments and Activities in Android programming?',
    'options': [
      ' Fragments are reusable UI components, while Activities represent app screens',
      ' Activities are reusable UI components, while Fragments represent app screens',
      ' Fragments are part of the Activity Lifecycle, while Activities are not',
      ' Activities are part of the Fragment Lifecycle, while Fragments are not'
    ],
    'answer':
    'A'
  }],
  'Chapter 10': [{
    'question':
    'Q24: What is the primary responsibility of a ViewHolder in RecyclerView?',
    'options': [
      ' To manage database connections', ' To handle network requests',
      ' To store and recycle views for efficient scrolling',
      ' To handle app permissions'
    ],
    'answer':
    'C'
  }],
  'Chapter 11': [{
    'question':
    'Q25: What is the difference between margins and padding in Android layouts?',
    'options': [
      ' Margins define the space outside the view, while padding defines the space inside the view',
      ' Padding defines the space outside the view, while margins define the space inside the view',
      ' Margins and padding are interchangeable terms',
      ' Margins define the space between views, while padding defines the space between the view\'s content and its boundaries'
    ],
    'answer':
    'A'
  }],
  'Chapter 12': [{
    'question':
    'Q26: What is the primary purpose of using coroutines in Android programming?',
    'options': [
      ' To manage app permissions',
      ' To handle asynchronous code execution',
      ' To store UI-related data', ' To manage database connections'
    ],
    'answer':
    'B'
  }],
  'Chapter 13': [{
    'question':
    'Q27: What does "Unidirectional Data Flow" mean in the context of Android programming?',
    'options': [
      ' Data flows in a single direction from a source to a destination',
      ' Data flows in multiple directions between sources and destinations',
      ' Data flows in a loop between sources and destinations',
      ' Data flows in a hierarchical structure between sources and destinations'
    ],
    'answer':
    'A'
  }],
  'Chapter 14': [{
    'question':
    'Q28: What is the purpose of serialization in Android programming?',
    'options': [
      ' To convert an object into a format suitable for storage or transmission',
      ' To create a deep copy of an object',
      ' To compare two objects for equality',
      ' To manage the memory allocated for an object'
    ],
    'answer':
    'A'
  }],
  'Chapter 15': [{
    'question':
    'Q29: Which of the following is a characteristic of an overflow menu in Android programming?',
    'options': [
      ' Appears on the app bar',
      ' Displays a list of all available actions',
      ' Can be accessed by pressing the three little dots',
      ' All of the above'
    ],
    'answer':
    'D'
  }],
  'Chapter 16': [{
    'question':
    'Q30: Which of the following is NOT part of an Implicit Intent in Android programming?',
    'options': [' Action', ' Data', ' Category', ' Component name'],
    'answer':
    'D'
  }],
  'Chapter 1: GeoQuiz': [{
    'question':
    'What is the purpose of the "Toast" class in Android development?',
    'options': [
      ' Displaying notifications or short messages to the user',
      ' Handling activity lifecycle events',
      ' Wiring up views in a layout', ' Creating layouts using XML'
    ],
    'answer':
    'A'
  }],
  'Chapter 2: GeoQuiz': [{
    'question':
    'How does wiring up views work using ViewBinding?',
    'options': [
      ' It automatically generates code for accessing views in a layout',
      ' Views are manually instantiated and connected to layout XML files',
      ' ViewBinding is not used for wiring up views',
      ' Views are wired up using the "Toast" class'
    ],
    'answer':
    'A'
  }, {
    'question':
    'Which unit of measurement is commonly used for specifying text size in Android?',
    'options': [' ps', ' dp', ' sp', ' in'],
    'answer': 'C'
  }],
  'Chapter 3: GeoQuiz': [{
    'question':
    'How can log functions be used to monitor the activity lifecycle?',
    'options': [
      ' By displaying toast messages',
      ' By printing log messages to the logcat',
      ' By changing the layout of the activity dynamically',
      ' By triggering explicit intents'
    ],
    'answer':
    'B'
  }],
  'Chapter 4: GeoQuiz': [{
    'question':
    'What is a potential issue associated with improper handling of ViewModel instances?',
    'options': [
      ' Memory leak', ' ReverseDNS lookup failure',
      ' Incompatible layout design', ' Invalid R class reference'
    ],
    'answer':
    'A'
  }],
  'Chapter 7: GeoQuiz': [{
    'question':
    'How can an activity start another activity using an explicit intent?',
    'options': [
      ' By calling the `startActivity(Intent)` method',
      ' By using theContext` class', ' By using the Intent Extras',
      ' By defining a companion object'
    ],
    'answer':
    'A'
  }],
  'Chapter 9: CriminalIntent': [{
    'question':
    'What is the primary difference between fragments and activities?',
    'options': [
      ' Fragments cannot be added dynamically at runtime',
      ' Fragments do not have their own lifecycle',
      ' Activities are used for UI components, while fragments are used for non-UI tasks',
      ' Activities are tied to a specific screen, while fragments can be reused in multiple screens'
    ],
    'answer':
    'D'
  }],
  'Chapter 10: CriminalIntent': [{
    'question':
    'What is the purpose of RecyclerView in Android development?',
    'options': [
      ' It is used for managing the lifecycle of fragments',
      ' It provides a way to display a scrollable list of items efficiently',
      ' RecyclerView is used for data serialization',
      ' It is responsible for handling explicit intents'
    ],
    'answer':
    'B'
  }, {
    'question':
    'Which method(s) must be overridden when creating a custom adapter for RecyclerView?',
    'options': [
      ' onCreateViewHolder()', ' onBindViewHolder()', ' getItemCount()',
      ' All of the above'
    ],
    'answer':
    'D'
  }],
  'Chapter 11: CriminalIntent': [{
    'question':
    'In ConstraintLayout, what does the "match_parent" option do?',
    'options': [
      ' It makes the view\'s size match the size of its parent layout',
      ' It sets the view\'s size to a fixed value in pixels',
      ' It adjusts the view\'s size based on its content',
      ' None of the above'
    ],
    'answer':
    'A'
  }, {
    'question':
    'What is the difference between margins and padding in Android layouts?',
    'options': [
      ' Margins define the space outside the view, while padding defines the space inside the view',
      ' Margins define the space inside the view, while padding defines the space outside the view',
      ' Margins and padding are interchangeable terms in Android layouts',
      ' Margins and padding have the same effect on the layout'
    ],
    'answer':
    'A'
  }],
  'Chapter 12: CriminalIntent': [{
    'question':
    'What is a coroutine in Kotlin?',
    'options': [
      ' A design pattern for managing database operations',
      ' A type of animation used for visual effects',
      ' A lightweight thread-like structure for asynchronous programming',
      ' A method for defining entity classes in Room'
    ],
    'answer':
    'C'
  }, {
    'question':
    'Which step is NOT part of creating a database with Room?',
    'options': [
      ' Defining entities', ' Implementing type converters',
      ' Defining a DAO (Data Access Object)',
      ' Initializing singleton Application classes'
    ],
    'answer':
    'D'
  }],
  'Chapter 13: CriminalIntent': [{
    'question':
    'How can fragment navigation be performed in Android?',
    'options': [
      ' By calling the `findNavController().navigate()` method',
      ' By using the Intent class', ' By using the GlobalScope',
      ' By registering for activity results with `ActivityResultContracts.StartActivityForResult`'
    ],
    'answer':
    'A'
  }, {
    'question':
    'What are safeArgs in Android navigation?',
    'options': [
      ' Arguments that can be passed between fragments safely',
      ' Special permissions required for fragment transactions',
      ' A type of interpolator used for animations',
      ' The navigation graph file for fragment navigation'
    ],
    'answer':
    'A'
  }],
  'Chapter 14: CriminalIntent': [{
    'question':
    'Which class can be used for handling dates and times in Java and Android?',
    'options':
    [' GregorianCalendar', ' Retrofit', ' ViewModel', ' RecyclerView'],
    'answer':
    'A'
  }],
  'Chapter 15: CriminalIntent': [{
    'question':
    'What is the purpose of an app bar in Android?',
    'options': [
      ' It provides a space for displaying application-specific actions or menus',
      ' It manages the layout of fragments in the activity',
      ' It defines the overall theme and style of the application',
      ' It handles the back navigation within the app'
    ],
    'answer':
    'A'
  }, {
    'question':
    'Which attribute is used to specify the behavior of menu items in the app bar?',
    'options':
    [' ifRoom', ' withText', ' overflow menu', ' All of the above'],
    'answer':
    'D'
  }],
  'Chapter 16: CriminalIntent': [{
    'question':
    'What are implicit intents in Android?',
    'options': [
      ' Intents that are declared in the manifest file',
      ' Intents that are created and explicitly defined in code',
      ' Intents that are used for inter-process communication',
      ' Intents that do not specify a particular component to start'
    ],
    'answer':
    'D'
  }, {
    'question':
    'What is data migration in the context of Android development?',
    'options': [
      ' The process of transferring data between databases',
      ' The process of updating an app\'s data format or structure',
      ' The process of encrypting sensitive data',
      ' The process of compressing data for storage optimization'
    ],
    'answer':
    'B'
  }],
  'Chapter 20: PhotoGallery': [{
    'question':
    'What is Retrofit used for in Android development?',
    'options': [
      ' Handling network requests and REST API communication',
      ' Parsing JSON data', ' Managing database operations with Room',
      ' Displaying images with Coil library'
    ],
    'answer':
    'A'
  }, {
    'question':
    'Which library is commonly used for parsing JSON in Android?',
    'options': [' Moshi', ' Retrofit', ' Coil', ' DataStore'],
    'answer':
    'A'
  }],
  'Chapter 21: PhotoGallery': [{
    'question':
    'What is an Interceptor in the context of network requests?',
    'options': [
      ' A mechanism for handling permission requests',
      ' A class responsible for intercepting and modifying network requests and responses',
      ' An Android component used for navigation between fragments',
      ' A design pattern for managing database operations'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What is DataStore in Android?',
    'options': [
      ' A library for handling image loading and caching',
      ' A storage solution for app-specific key-value data',
      ' A utility class for creating animations',
      ' An architecture component for managing UI-related data'
    ],
    'answer':
    'B'
  }],
  'Chapter 24: One-Shot': [{
    'question':
    'Which method is commonly overridden to handle touch events in a custom View?',
    'options': [
      ' onTouchEvent()', ' onDraw()', ' invalidate()',
      ' requestLayout()'
    ],
    'answer':
    'A'
  }, {
    'question':
    'What does the "invalidate()" method do in Android?',
    'options': [
      ' Invalidates the current layout and triggers a redraw',
      ' Invalidates the current View object and releases system resources',
      ' Invalidates the current data in a database',
      ' Invalidates the current thread and restarts its execution'
    ],
    'answer':
    'A'
  }],
  'Chapter 25: One-Shot': [{
    'question':
    'What is ObjectAnimator used for in Android animations?',
    'options': [
      ' Playing audio files',
      ' Animating object properties, such as position or size',
      ' Creating custom interpolators',
      ' Loading and caching images from the network'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What is the purpose of the "by lazy" syntax in Kotlin?',
    'options': [
      ' It declares a lazy property that is initialized only when accessed for the first time',
      ' It specifies the duration of an animation',
      ' It defines a custom interpolator for animations',
      ' It creates a new instance of a class using the Builder pattern'
    ],
    'answer':
    'A'
  }],
  'Chapter N: ActivityManager and Intents': [{
    'question':
    'What is the purpose of the ActivityManager in Android?',
    'options': [
      ' Handles database operations',
      ' Manages activities and their lifecycle',
      ' Controls animations and transitions',
      ' Provides utility functions for network operations'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What is a Context in Android?',
    'options': [
      ' A utility for handling network requests',
      ' A class that provides application-level operations and access to resources',
      ' A class responsible for managing database operations',
      ' A class for handling touch events and user inputs'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What is the purpose of intent extras in Android?',
    'options': [
      ' To manage memory and optimize app performance',
      ' To provide additional data when sending intents between components',
      ' To handle user permissions and security features',
      ' To control application themes and styles'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What is a companion object in Kotlin?',
    'options': [
      ' A utility for creating and managing threads',
      ' An object that allows access to functions without having an instance of the class',
      ' A way to create singletons in Kotlin',
      ' A design pattern for handling complex object creation'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What is the purpose of setResult() in Android activities?',
    'options': [
      ' To send back results and data from child activities to their parent activities',
      ' To set the layout and appearance of an activity',
      ' To handle user input and touch events',
      ' To manage the activity stack and handle navigation'
    ],
    'answer':
    'A'
  }, {
    'question':
    'What is the purpose of back binding in Android development?',
    'options': [
      ' To bind UI elements in Android XML layouts to Kotlin properties',
      ' To optimize memory management by freeing (nulling) view references in onDestroyView()',
      ' To store the value of a property with custom getter and/or setter logic',
      ' To create singletons and manage object instances'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What is viewLifecycleOwner.repeatOnLifecycle used for?',
    'options': [
      ' To create a database with Room',
      ' To execute coroutine code while the fragment is in a specified lifecycle state',
      ' To define entities in a database',
      ' To access navigation arguments once the user is at their destination'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What are the 3 steps to creating a database with Room?',
    'options': [
      ' Annotate model class to make it a database entry, create a type converter, and define entities',
      ' Create the class which will represent the database itself, create a type converter, and define entities',
      ' Annotate model class to make it a database entry, create the class which will represent the database itself, and create a type converter',
      ' Define entities, create a type converter, and create the class which will represent the database itself'
    ],
    'answer':
    'C'
  }, {
    'question':
    'What is a DAO?',
    'options': [
      ' A type of database entry',
      ' An interface that contains functions for each database operation we want to perform',
      ' A tool for observing changes to a database as they occur',
      ' A design pattern that isolates the data layer from the rest of the app'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What is the purpose of viewModelScope.launch {} in Android?',
    'options': [
      ' To handle user input and touch events',
      ' To create a database with Room',
      ' To launch a coroutine and enable calling suspending functions within the code block',
      ' To define entities in a database'
    ],
    'answer':
    'C'
  }, {
    'question':
    'What does viewLifecycleOwner.launch signify in Android development?',
    'options': [
      ' It indicates that the class will have a lifecycle and allows the use of repeatOnLifecycle',
      ' It creates a new instance of a ViewModel',
      ' It initializes the database with Room',
      ' It starts an animation or transition'
    ],
    'answer':
    'A'
  }, {
    'question':
    'What is the main purpose of Flow in Kotlin?',
    'options': [
      ' To create a single stream of data and cache results',
      ' To handle user input and touch events',
      ' To provide an asynchronous stream of data, useful for observing changes to a database as they occur',
      ' To manage memory and optimize app performance'
    ],
    'answer':
    'C'
  }, {
    'question':
    'What is the primary advantage of StateFlow over Flow in Kotlin?',
    'options': [
      ' StateFlow maintains a single stream of data from the database and caches results for quick display',
      ' StateFlow handles user input and touch events more efficiently',
      ' StateFlow provides better memory management and optimization',
      ' StateFlow simplifies the process of binding UI elements to Kotlin properties'
    ],
    'answer':
    'A'
  }, {
    'question':
    'What is the main characteristic of GlobalScope in Kotlin coroutines?',
    'options': [
      ' It operates only within a specific fragment or activity',
      ' It is a coroutine scope that is available globally and operates throughout the entire application lifecycle',
      ' It is used to create database instances with Room',
      ' It is a scope that automatically cancels launched work when the containing fragment or activity is destroyed'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What is the main purpose of data migration in Room?',
    'options': [
      ' To handle user input and touch events',
      ' To create a new instance of a ViewModel',
      ' To tell Room how to manage changes to the database structure so it stays in sync with database entity classes',
      ' To manage memory and optimize app performance'
    ],
    'answer':
    'C'
  }, {
    'question':
    'What are the main components of an implicit intent in Android?',
    'options': [
      ' Action, location of data, type of data, and optional categories',
      ' Duration, interpolator, and view to be animated',
      ' Source, destination, and navigation arguments',
      ' Database entity, DAO, and version number'
    ],
    'answer':
    'A'
  }, {
    'question':
    'How do you request network access permission in an Android application?',
    'options': [
      ' By calling the requestPermissions() method in the activity',
      ' By adding the permission request to the manifest using the <uses-permission> tag',
      ' By creating a custom dialog to prompt the user for permission',
      ' By using the getSystemService() method to obtain the ConnectivityManager'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What are the main features of the Coil library in Android development?',
    'options': [
      ' Loading and binding images, adding placeholders, and applying transformations',
      ' Managing database operations and data migrations',
      ' Handling network requests and REST API communication',
      ' Creating and managing ViewModel instances'
    ],
    'answer':
    'A'
  }, {
    'question':
    'What is the purpose of the onDraw(Canvas) method in a custom View?',
    'options': [
      ' To change the background color and draw custom elements on the screen',
      ' To handle touch events and gestures',
      ' To manage the lifecycle of the View',
      ' To load and display images from a network source'
    ],
    'answer':
    'A'
  }, {
    'question':
    'What does the "invalidate()" method do in the context of a custom BoxDrawingView?',
    'options': [
      ' It triggers the View to redraw itself',
      ' It cancels a currently running animation',
      ' It creates a new instance of the View',
      ' It starts an animation on the View'
    ],
    'answer':
    'A'
  }, {
    'question':
    'What is the main purpose of using an ObjectAnimator in Android animations?',
    'options': [
      ' To load and display images from a network source',
      ' To repeatedly call setter functions with different values, animating object properties',
      ' To manage the lifecycle of an Activity or Fragment',
      ' To handle touch events and gestures on a custom View'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What is the purpose of using "by lazy" in Kotlin?',
    'options': [
      ' To create a new instance of a class using the Builder pattern',
      ' To define a lazy property that is initialized only when accessed for the first time',
      ' To specify the duration of an animation',
      ' To create a custom interpolator for animations'
    ],
    'answer':
    'B'
  }, {
    'question':
    'What is the role of an interpolator in Android animations?',
    'options': [
      ' To load and display images from a network source',
      ' To handle touch events and gestures on a custom View',
      ' To manage the lifecycle of an Activity or Fragment',
      ' To change the way an animation progresses between its start and end points'
    ],
    'answer':
    'D'
  }, {
    'question':
    'What is the main advantage of using an AnimatorSet in Android animations?',
    'options': [
      ' To manage the lifecycle of an Activity or Fragment',
      ' To load and display images from a network source',
      ' To handle touch events and gestures on a custom View',
      ' To group and play animations together in a synchronized or sequential manner'
    ],
    'answer':
    'D'
  }]
}


def main():
    print("Android Development Quiz")
    print("-------------------------")

    correct_answers = 0
    total_questions = sum(len(questions) for questions in study_guide.values())

    chapters = list(study_guide.keys())
    remaining_questions = {
        chapter: set(range(len(study_guide[chapter])))
        for chapter in chapters
    }

    try:
        while sum(len(questions) for questions in remaining_questions.values()) > 0:
            chapter = random.choice(chapters)
            if not remaining_questions[chapter]:
                chapters.remove(chapter)
                continue

            question_index = random.choice(list(remaining_questions[chapter]))
            remaining_questions[chapter].remove(question_index)
            question = study_guide[chapter][question_index]

            # Jumble around the options while keeping track of the correct answer
            options = question['options']
            correct_option_index = ord(question['answer']) - ord('A')
            correct_option = options[correct_option_index]

            shuffled_options = list(enumerate(options))
            all_of_the_above = None

            if " All of the above" in options:
                all_of_the_above_index = options.index(" All of the above")
                all_of_the_above = shuffled_options.pop(all_of_the_above_index)

            random.shuffle(shuffled_options)

            if all_of_the_above:
                shuffled_options.append(all_of_the_above)

            new_correct_option_index = shuffled_options.index((correct_option_index, correct_option))

            # Update the answer to reflect the shuffled options
            question['answer'] = chr(ord('A') + new_correct_option_index)

            print(f"{chapter}: {question['question']}\n")
            for index, (_, option) in enumerate(shuffled_options):
                print(f"{chr(ord('A') + index)}) {option}")

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


