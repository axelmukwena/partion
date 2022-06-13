# Partion, Partnership - Suggestion
 Implementation for a Partnership Suggestion service for Reveal Companies as per [requirements](https://github.com/reveal-co/hiring/tree/master/backend)

## Challenges encountered
- At my current job, programmatic tests are not required thus my implementation is hacky and I will definitely need to practice and review more.
- I'm also more experienced with Ruby on Rails's out-of-the-box's implementation which tends to limit the logic, code structure and organization of the application. Thus, I had to spend some time reading up on the different types of Implementation Architectures, including Hexagonal.
- Future reviews include reorganization of the file structure suitable for scaling and matching the needs of the implementation, rather than conforming to the structure of traditional web apps / APIs

current structure
```shell
--- app
     |--- adapters
     |--- domain
     |--- entities
     |--- models
--- tests
```

alternative structure
```shell
--- service1
     |--- tests.py
     |--- models.py
     |--- logic.py
     |--- adapters
--- service2
     |--- ...
```

### Did not have time to...

- I did not fully understand the usability of some elements though the requirements and process flow was very clear, which did not hinder the execution of the test. For instance:
    1. In the requirements, no 6: the statement [_for the title, content and recipients of the email to be sent_] did not explicitly state the difference between recipients and emails. 
    2. Each company has multiple recipients, where each recipient received the same Title and Content?
    3. I also did not fully understand what _email_type_ evaluates to?

### Running the program

Before executing the program, you're expected to toggle the comment between raise and return statements in all the entity and adapter files

`raise NotImplemented` | as per hiring test requirements <br>
`return` | as per testing requirements

#### NB: No external packages used, only Builtin functions were used. So no need to run the following instructions.

- Developed using Python 3.9 on Unix based MacOS Catalina
- Seamlessly tested using Intellij Pycharm
- It took me around 5-6 hours, including testing, comments and How-To
- Helpful resources:
    1. https://douwevandermeij.medium.com/hexagonal-architecture-in-python-7468c2606b63
    2. https://github.com/bjudson/topsy/tree/0a183e95d2c5b2eefcc4888a1f6ef5085e419691
    3. https://medium.com/@vsavkin/hexagonal-architecture-for-rails-developers-8b1fee64a613

To continue, clone the repository and navigate its directory

      $ cd folder/partion
      
- Install virtualenv
      
      # Mac OS
      $ sudo -H pip install virtualenv
      
      # Windows
      $ pip install virtualenv
  
- Create a virtual environment
  
      # Mac OS
      $ virtualenv -p python3 venv

      # Windows
      $ python3 -mvenv venv
      
- Activate the environment
  
      # Mac OS
      $ source venv/bin/activate
      
      # Windows
      $ venv\Scripts\activate

- Install the requirements.txt, skip this stage
  
      # Mac OS
      $ pip3 install -r requirements.txt
      
      # Windows
      $ python3 -m pip install -r requirements.txt
    
- Run the test scripts...

      $ python3 tests/adapters_tests.py
      $ python3 tests/suggestions_domain_tests.py
      $ python3 tests/suggestions_entities_tests.py


### Developer Notes

- Go to folder

      $ cd folder/partion

- Activate env

      # Mac OS
      $ source venv/bin/activate

      # Windows
      $ venv\Scripts\activate
  
- Install or update package

      # specific command
      # MacOS
      $ pip install --upgrade package

- Update *requirements.txt*

      $ pip freeze > requirements.txt

### Deactivate env
- Deactivate env

      # Mac OS
      $ deactivate

      # Windows
      $ 
