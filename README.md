# Partion, Partnership - Suggestion
 Implementation for a Partnership Suggestion service for Reveal Companies as per [requirements](https://github.com/reveal-co/hiring/tree/master/backend)

### Running the program

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