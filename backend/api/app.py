import sys
import os
# Add the parent directory (backend) to sys.path so that config.py can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, jsonify, abort
from flask_cors import CORS
import base64
from config import DevelopmentConfig, ProductionConfig

app = Flask(__name__)
CORS(app)

# Decide which configuration to use based on an environment variable
if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)

# Endpoint to return the base URL from the configuration
@app.route('/api-base-url')
def get_api_base_url():
    return app.config['BASE_URL']

def get_asset_path(filename):
    # Get the absolute path of the assets folder relative to this file.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Assuming the assets folder is one level up from the api folder
    return os.path.join(base_dir, '..', 'assets', filename)

def encode_image_to_base64(filename):
    """Encode an image file to a base64 string using an absolute path."""
    image_path = get_asset_path(filename)
    try:
        with open(image_path, 'rb') as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"File not found: {image_path}")  # Helpful error logging
        return None


@app.route('/api/projects')
def get_projects():
    projects = [
        {
            "id": 1,
            "title": "Atlas",
            "image": encode_image_to_base64('../assets/atlas.png') ,
            "description": "Atlas is a web application that allows users to create and manage projects. The application is built using the MERN stack and features user authentication, project management, and task tracking.",
            "details": """naumana.contractor@atlashxm.com
\n• Worked on projects named TimeAndAttendance, AskAnExpert and CoreHR, modules used by Atlas 
configured by micro-frontend architecture for clients such as Toyota, BathandBodyWorks, Luxoft, Coupa, 
Sensia, Namely, CIN7, etc. 
\n• Collaborate with on-the-ground entities in over 160 countries to streamline and ensure compliance 
with global expansion efforts. 
\n• Wrote comprehensive unit tests using React Testing Library and Jest. 
\n• Developed various complex forms with user validation using Yup and FormIk. 
\n• Worked with Restful APIs and JWT web tokens, handled deployments in pipelines, and used modules 
federation to maintain loose coupling. 
\n• Contributed to the company's internal Storybook library and continuously added new reusable 
components that can be used across all team verticals. 
\n• Regularly provided constructive PR feedback and encouraged collaboration to strengthen team bonds. 
Technologies used: HTML5 | CSS3 | Tailwind | Typescript | JavaScript | React | Redux | Hooks | Context API | 
Yup | FormIk | Git | Figma | Unit Testing | Rest APIs | Webpack | ESLint | SonarQube | custom hooks""",
        },
        {"id": 2, "title": "Benefits GPT", "image": encode_image_to_base64('../assets/quantum_sim_mini_logo.png') , "description": "Benefits GPT (Product of Quantumgears) is a web application that generates benefit summaries for employees. The application uses OpenAI's GPT-3 API to generate text based on user inputs.",
         "details": """ 
mnauman@quantumgears.com
\n• Sole front-end developer for a US AI-based startup building products such as SecureGPT, BenefitsGPT, and 
ContractualGPT. 
\n• Delivered the first module’s UI in few weeks, leading the development of key project modules from 
scratch. 
\n• Implemented comprehensive unit tests using React Testing Library and Jest, ensuring high code quality. 
\n• Modernized the repository with Tailwind CSS and ShadCN based on Radix UI for scalable, maintainable 
design. 
\n• Contributed to back-end development using Node.js, ensuring seamless integration and support. 
\n• Delivered high-quality scalable code with loose coupling. 
\n• Regularly provided constructive PR feedback and encouraged collaboration to strengthen team bonds. 
Technologies used: Tailwind | Typescript | JavaScript | React | Redux | Hooks | Context API | react query | 
React form hook | Git | Figma | Unit Testing | Rest APIs | Webpack | ESLint | SonarQube | custom hooks| 
Node js
"""
          },
        {"id": 3, "title": "Secure GPT", "image": encode_image_to_base64('../assets/quantum_sim_mini_logo.png') , "description": "Secure GPT (Product of Quantumgears) is a web application that allows users to encrypt and decrypt text using GPT-3. The application uses symmetric encryption algorithms to secure user data." ,
         "details": """ 
mnauman@quantumgears.com
\n• Sole front-end developer for a US AI-based startup building products such as SecureGPT, BenefitsGPT, and 
ContractualGPT. 
\n• Delivered the first module’s UI in few weeks, leading the development of key project modules from 
scratch. 
\n• Implemented comprehensive unit tests using React Testing Library and Jest, ensuring high code quality. 
\n• Modernized the repository with Tailwind CSS and ShadCN based on Radix UI for scalable, maintainable 
design. 
\n• Contributed to back-end development using Node.js, ensuring seamless integration and support. 
\n• Delivered high-quality scalable code with loose coupling. 
\n• Regularly provided constructive PR feedback and encouraged collaboration to strengthen team bonds. 
Technologies used: Tailwind | Typescript | JavaScript | React | Redux | Hooks | Context API | react query | 
React form hook | Git | Figma | Unit Testing | Rest APIs | Webpack | ESLint | SonarQube | custom hooks| 
Node js
"""},
        {"id": 4, "title": "Contracts GPT", "image": encode_image_to_base64('../assets/quantum_sim_mini_logo.png') , "description": "Contracts GPT (Product of Quantumgears) is a web application that generates legal contracts models based on user input and the contracts between join ventures and companies. The application uses OpenAI's GPT-3 API to generate contract templates.",
         "details": """ 
mnauman@quantumgears.com
\n• Sole front-end developer for a US AI-based startup building products such as SecureGPT, BenefitsGPT, and 
ContractualGPT. 
\n• Delivered the first module’s UI in few weeks, leading the development of key project modules from 
scratch. 
\n• Implemented comprehensive unit tests using React Testing Library and Jest, ensuring high code quality. 
\n• Modernized the repository with Tailwind CSS and ShadCN based on Radix UI for scalable, maintainable 
design. 
\n• Contributed to back-end development using Node.js, ensuring seamless integration and support. 
\n• Delivered high-quality scalable code with loose coupling. 
\n• Regularly provided constructive PR feedback and encouraged collaboration to strengthen team bonds. 
Technologies used: Tailwind | Typescript | JavaScript | React | Redux | Hooks | Context API | react query | 
React form hook | Git | Figma | Unit Testing | Rest APIs | Webpack | ESLint | SonarQube | custom hooks| 
Node js
""" },
        {"id": 5, "title": "SECP", "image": encode_image_to_base64('../assets/secp.png') , "description": "SECP is a web application that allows users to create and manage secure passwords. The application uses cryptographic algorithms to generate and store passwords.",
         "details": """
\n• Played a key role in projects for the Securities and Exchange Commission of Pakistan (SECP), a major 
government initiative. 
\n• Contributed to SECP's mission to register all companies operating in Pakistan, including local and foreign 
entities. 
\n• Worked within the framework established by the Securities and Exchange Commission of Pakistan Act, 1997, 
supporting SECP's administrative authority and financial independence in executing its regulatory and 
statutory responsibilities.
Technologies used: HTML5 | CSS3 | Tailwind | Typescript | JavaScript | React | Angular | Redux | Hooks | 
Context API | Kendo | RxJs | Formly | Pipes | Dynamic forms | Observables |Yup | FormIk | Git | Figma | Unit 
Testing | Rest APIs | Webpack | ESLint | SonarQube | custom hooks
 """
          },
        {"id": 6, "title": "Custom Behavior GPT", "image": encode_image_to_base64('../assets/quantum_sim_mini_logo.png') , "description": "Custom Behavior GPT (Product of Quantumgears) is a web application that generates custom behavior models for AI agents. The application uses OpenAI's GPT-3 API to generate behavior models.",
         "details": """ 
mnauman@quantumgears.com
\n• Sole front-end developer for a US AI-based startup building products such as SecureGPT, BenefitsGPT, and 
ContractualGPT. 
\n• Delivered the first module’s UI in few weeks, leading the development of key project modules from 
scratch. 
\n• Implemented comprehensive unit tests using React Testing Library and Jest, ensuring high code quality. 
\n• Modernized the repository with Tailwind CSS and ShadCN based on Radix UI for scalable, maintainable 
design. 
\n• Contributed to back-end development using Node.js, ensuring seamless integration and support. 
\n• Delivered high-quality scalable code with loose coupling. 
\n• Regularly provided constructive PR feedback and encouraged collaboration to strengthen team bonds. 
Technologies used: Tailwind | Typescript | JavaScript | React | Redux | Hooks | Context API | react query | 
React form hook | Git | Figma | Unit Testing | Rest APIs | Webpack | ESLint | SonarQube | custom hooks| 
Node js
""" },
        # ... more projects
    ]
    return jsonify(projects)



@app.route('/api/getProjectDetails/<int:id>')
def get_project_details(id):
    projects = {
        1: {
            "title": "Atlas",
            "description": "Atlas is a web application that allows users to create and manage projects. The application is built using the MERN stack and features user authentication, project management, and task tracking.",
            "image_path": "../assets/project_atlas.jpg",
            "technologies": ["React", "Node.js", "Express", "MongoDB"],
            "demo": "https://atlas-demo.com",
            "source": ""
        },
        2: {
            "title": "Benefits GPT",
            "description": "Benefits GPT is a web application that generates benefit summaries for employees. The application uses OpenAI's GPT-3 API to generate text based on user inputs.",
            "image_path": "assets/project2.jpg",
            "technologies": ["React", "Flask", "OpenAI GPT-3"],
            "demo": "https://benefits-gpt.com",
            "source": ""
        },
        3: {
            "title": "Secure GPT",
            "description": "Secure GPT is a web application that allows users to encrypt and decrypt text using GPT-3. The application uses symmetric encryption algorithms to secure user data.",
            "image_path": "assets/project3.jpg",
            "technologies": ["React", "Flask", "OpenAI GPT-3"],
            "demo": "https://secure-gpt.com",
            "source": ""
        },
        4: {
            "title": "Contracts GPT",
            "description": "Contracts GPT is a web application that generates legal contracts based on user input. The application uses OpenAI's GPT-3 API to generate contract templates.",
            "image_path": "assets/project4.jpg",
            "technologies": ["React", "Flask", "OpenAI GPT-3"],
            "demo": "https://contracts-gpt.com",
            "source": ""
        },
        5: {
            "title": "SECP",
            "description": "SECP is a web application that allows users to create and manage secure passwords. The application uses cryptographic algorithms to generate and store passwords.",
            "image_path": "assets/project5.jpg",
            "technologies": ["React", "Flask", "Cryptography"],
            "demo": "https://secp.com",
            "source": ""
        },
        6: {
            "title": "Custom Behavior GPT",
            "description": "Custom Behavior GPT is a web application that generates custom behavior models for AI agents. The application uses OpenAI's GPT-3 API to generate behavior models.",
            "image_path": "assets/project6.jpg",
            "technologies": ["React", "Flask", "OpenAI GPT-3"],
            "demo": "https://custom-behavior-gpt.com",
            "source": ""
        },
        # ... more projects
    }

    if id not in projects:
        abort(404)

    project = projects[id]
    # Encode the image to a base64 string using the image_path value
    encoded_image = encode_image_to_base64(project["image_path"])
    if encoded_image:
        project["image"] = encoded_image
    else:
        # Fallback: return the original path if file not found
        project["image"] = project["image_path"]

    # Optionally remove the image_path key from the output
    project.pop("image_path", None)
    
    return jsonify(project)


@app.route('/api/getProfilePicture')
def get_profile_picture():
    return jsonify({"image": encode_image_to_base64('../assets/profilePicture.jpg')})

@app.route('/api/getAboutDescription')
def get_about_description():
    description = " I am a dedicated Software Engineer with over 3 years of experience in full-stack development. Specializing in modern JavaScript frameworks like MERN stack, Next js and Python, I have collaborated with multinational corporations and government agencies on impactful projects. My expertise in unit testing, UI/UX design, and Agile methodologies drives innovation and excellence."
    return jsonify({"description": description})


# def handler(event, context):
#     return handle_request(app, event, context)

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    app.run()

