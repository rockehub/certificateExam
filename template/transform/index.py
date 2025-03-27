import json

def transform_questions(questions):
    transformed = []
    
    for question in questions:
        transformed_options = [
            {"number": i + 1, "question": option} for i, option in enumerate(question["Options"])
        ]
        
        transformed.append({
            "Question": question["Question"],
            "QuestionText": question["QuestionText"],
            "Options": transformed_options,
            "CorrectAnswer": question["CorrectAnswer"]
        })
    
    return transformed

# Exemplo de uso
original_data = {
  "name": "SAP BTP",
  "id": "SAP_BTP",
  "min_required": 21,
  "max_questions": 30,
  "questions": [
    {
      "Question": "1",
      "QuestionText": "Which of the following are functions of the SAP AppRouter? (Select all correct answers)",
      "Options": [
        "1.) Load balancing and traffic distribution",
        "2.) Authentication and authorization",
        "3.) Data storage and retrieval",
        "4.) UI rendering and design"
      ],
      "CorrectAnswer": "1,2"
    },
    {
      "Question": "2",
      "QuestionText": "To set up trust and authorization for an SAP BTP application, which steps are involved? (Select all correct answers)",
      "Options": [
        "1.) Creating a new user for each application instance",
        "2.) Configuring roles and&nbsp; permissions in the application manifest",
        "3.) Defining security rules in the SAP Cloud Platform cockpit",
        "4.) Implementing OAuth 2.0 for authentication"
      ],
      "CorrectAnswer": "2,3"
    },
    {
      "Question": "3",
      "QuestionText": "Which of the following are valid identity providers for SAP BTP? (Select all correct answers)",
      "Options": [
        "1.) SAP Single Sign-On (SSO)",
        "2.) Google",
        "3.) Microsoft Azure Active Directory",
        "4.) Amazon Web Services (AWS)"
      ],
      "CorrectAnswer": "1,2,3"
    },
    {
      "Question": "4",
      "QuestionText": "What is the primary function of the approuter in an SAP BTP application architecture?",
      "Options": [
        "1.) Authenticating users and generating access tokens",
        "2.) Handling database queries and data storage",
        "3.) Creating user interfaces and frontend components.",
        "4.) Managing server-side logic and business processes"
      ],
      "CorrectAnswer": "1"
    },
    {
      "Question": "5",
      "QuestionText": "You are developing an SAP BTP application for a company that wants to implement single sign-on (SSO) with their existing Microsoft Azure Active Directory (Azure AD) identity provider. The company's employees should be able to log in to the SAP BTP application using their Azure AD credentials.What steps are required to achieve single sign-on integration with Azure AD in your SAP BTP application? (Select all that apply.)",
      "Options": [
        "1.) Configure the approuter to act as a frontend proxy",
        "2.) Exchange API documentation with Azure AD",
        "3.) Define routing rules in the \"xs-app.json\" file",
        "4.) Set up trust by exchanging security tokens with Azure AD",
        "5.) Implement role-based authorization in the frontend UI"
      ],
      "CorrectAnswer": "1,4"
    },
    {
      "Question": "6",
      "QuestionText": "You are designing an SAP BTP application that requires authentication and authorization through an external identity provider. You need to choose suitable identity providers based on the application's requirements.Which identity provider(s) would be appropriate for an SAP BTP application intended for internal use by company employees? (Select all that apply.)",
      "Options": [
        "1.) Google",
        "2.) SAP S/4HANA",
        "3.) Microsoft Azure Active Directory",
        "4.) GitHub",
        "5.) Okta"
      ],
      "CorrectAnswer": "2,3"
    },
    {
      "Question": "7",
      "QuestionText": "You are developing an SAP BTP application for an e-commerce platform. The application needs to implement different authorization rules for different user roles. Customers can view products and place orders, while administrators can manage inventory and customer accounts.Question 13: Where should you implement the authorization rules based on user roles in your SAP BTP application?",
      "Options": [
        "1.) Frontend user interface components",
        "2.) Identity Provider (IdP)",
        "3.) Backend services",
        "4.) approuter configuration"
      ],
      "CorrectAnswer": "3"
    },
    {
      "Question": "8",
      "QuestionText": "What is SAP Cloud Application Programming Model (CAP)?",
      "Options": [
        "1.) A cloud-based IDE for SAP developers",
        "2.) A development framework for building SAP Fiori applications",
        "3.) A comprehensive development model for cloud-native applications",
        "4.) A database management system for SAP HANA"
      ],
      "CorrectAnswer": "3"
    },
    {
      "Question": "9",
      "QuestionText": "Which programming languages can be used with SAP CAP?",
      "Options": [
        "1.) Java",
        "2.) Python",
        "3.) JavaScript/Node.js",
        "4.) Ruby"
      ],
      "CorrectAnswer": "3"
    },
    {
      "Question": "10",
      "QuestionText": "What is the purpose of the 'cds' folder in a CAP project?",
      "Options": [
        "1.) It contains JavaScript libraries",
        "2.) It defines the project's database schema",
        "3.) It stores configuration files",
        "4.) It houses CAP's UI components"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "11",
      "QuestionText": "Scenario: You want to create a Fiori application using CAP. What is the role of the 'app' folder in your project?",
      "Options": [
        "1.) It defines database tables",
        "2.) It contains UI-related files",
        "3.) It stores business logic",
        "4.) It is not related to Fiori applications"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "12",
      "QuestionText": "Scenario: You want to implement custom authentication and authorization in your CAP application. Which CAP feature allows you to achieve this?",
      "Options": [
        "1.) Middleware services",
        "2.) CDS views",
        "3.) Service definitions",
        "4.) CAP security policies"
      ],
      "CorrectAnswer": "4"
    },
    {
      "Question": "13",
      "QuestionText": "What role does the 'package.json' file play in a CAP project?",
      "Options": [
        "1.) It contains UI templates",
        "2.) It specifies project dependencies and scripts",
        "3.) It defines database tables",
        "4.) It is not relevant to CAP projects"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "14",
      "QuestionText": "Scenario: You want to perform advanced data transformations before exposing data through a CAP service. What CAP feature can you use for this purpose?",
      "Options": [
        "1.) CAP authorization",
        "2.) CDS views",
        "3.) Service events",
        "4.) UI components"
      ],
      "CorrectAnswer": "3"
    },
    {
      "Question": "15",
      "QuestionText": "Which of the following data sources can be integrated with SAP CAP? (Select all that apply.)",
      "Options": [
        "1.) SAP HANA",
        "2.) MySQL",
        "3.) Microsoft Excel",
        "4.) PostgreSQL"
      ],
      "CorrectAnswer": "1,2,4"
    },
    {
      "Question": "16",
      "QuestionText": "Scenario: You want to enable full-text search capabilities in your CAP application. Which CAP feature allows you to implement this functionality? (Select all that apply.)",
      "Options": [
        "1.) Full-text search module",
        "2.) Text analytics service",
        "3.) CAP security policies",
        "4.) Service definitions"
      ],
      "CorrectAnswer": "1,2"
    },
    {
      "Question": "17",
      "QuestionText": "Scenario: You are building a CAP application for a retail company. You need to model the product catalog. Which CAP artifacts would you use for this purpose? (Select all that apply.)",
      "Options": [
        "1.) Entity definitions",
        "2.) Service modules",
        "3.) CDS views",
        "4.) UI components"
      ],
      "CorrectAnswer": "1,3"
    },
    {
      "Question": "18",
      "QuestionText": "Scenario: In your CAP project, you want to create a calculated field that calculates the total price of an order based on the quantity and unit price. Which CAP feature should you use?",
      "Options": [
        "1.) Service modules",
        "2.) CDS views with calculated fields",
        "3.) UI components",
        "4.) Middleware services"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "19",
      "QuestionText": "Scenario: You want to expose OData and GraphQL services for your CAP application. Which CAP feature enables you to achieve this? (Select all that apply.)",
      "Options": [
        "1.) OData adapter",
        "2.) GraphQL module",
        "3.) Service definitions",
        "4.) CDS views"
      ],
      "CorrectAnswer": "1,2"
    },
    {
      "Question": "20",
      "QuestionText": "Scenario: You are building a CAP application for an e-commerce platform, and you need to create RESTful APIs for product search. What CAP artifact should you use?",
      "Options": [
        "1.) Service modules",
        "2.) CDS views",
        "3.) Entity definitions",
        "4.) UI components"
      ],
      "CorrectAnswer": "1"
    },
    {
      "Question": "21",
      "QuestionText": "Scenario: You need to implement complex business logic in your CAP application, such as pricing calculations or inventory management. What CAP feature allows you to encapsulate and execute such logic? (Select all that apply.)",
      "Options": [
        "1.) CDS views with calculated fields",
        "2.) Service modules",
        "3.) Middleware services",
        "4.) UI annotations"
      ],
      "CorrectAnswer": "1,3"
    },
    {
      "Question": "22",
      "QuestionText": "Scenario: Your CAP application needs to support advanced querying and filtering options for users. What CAP feature allows you to define and execute complex queries?",
      "Options": [
        "1.) CDS views with calculated fields",
        "2.) OData adapter",
        "3.) CAP security policies",
        "4.) Service definitions"
      ],
      "CorrectAnswer": "4"
    },
    {
      "Question": "23",
      "QuestionText": "Scenario: You want to enforce data validation rules in your CAP application to ensure data integrity. What CAP feature allows you to define and enforce validation rules?",
      "Options": [
        "1.) CAP authorization",
        "2.) CDS views with calculated fields",
        "3.) CAP security policies",
        "4.) Data annotations"
      ],
      "CorrectAnswer": "4"
    },
    {
      "Question": "24",
      "QuestionText": "Scenario: You need to implement a workflow in your CAP application where specific actions trigger events. What CAP feature is designed for this purpose?",
      "Options": [
        "1.) CAP authorization",
        "2.) CDS views with calculated fields",
        "3.) Service events",
        "4.) CAP security policies"
      ],
      "CorrectAnswer": "3"
    },
    {
      "Question": "25",
      "QuestionText": "Scenario: You have developed a CAP application, and you want to deploy it to both an on-premises environment and a cloud platform. What should you consider for successful deployment?",
      "Options": [
        "1.) Adhering to cloud-only deployment",
        "2.) Using service modules exclusively",
        "3.) Making use of CAP security policies",
        "4.) Ensuring compatibility with both environments"
      ],
      "CorrectAnswer": "4"
    },
    {
      "Question": "26",
      "QuestionText": "Scenario: Your CAP application deals with a large amount of textual data, and you want to implement full-text search capabilities. What CAP features can be used to enable full-text search? (Select all that apply.)",
      "Options": [
        "1.) Full-text search module",
        "2.) Text analytics service",
        "3.) CAP security policies",
        "4.) Service events"
      ],
      "CorrectAnswer": "1,2"
    },
    {
      "Question": "27",
      "QuestionText": "Which of the following is a common CI/CD tool used in SAP environments?",
      "Options": [
        "1.) Jenkins",
        "2.) Microsoft Excel",
        "3.) Adobe Photoshop",
        "4.) Google Chrome"
      ],
      "CorrectAnswer": "1"
    },
    {
      "Question": "28",
      "QuestionText": "What is the primary benefit of automated testing in CI/CD pipelines?",
      "Options": [
        "1.) Reducing the need for version control",
        "2.) Ensuring 100% code coverage",
        "3.) Detecting issues early in the development process",
        "4.) Replacing manual code reviews"
      ],
      "CorrectAnswer": "3"
    },
    {
      "Question": "29",
      "QuestionText": "Which of the following is a common tool used for containerization in CI/CD processes?",
      "Options": [
        "1.) Docker",
        "2.) Jenkins",
        "3.) Git",
        "4.) JIRA"
      ],
      "CorrectAnswer": "1"
    },
    {
      "Question": "30",
      "QuestionText": "What practice involves freezing changes to the codebase for a specific period, typically before a major release?",
      "Options": [
        "1.) Blue-green deployment",
        "2.) Code freeze",
        "3.) Canary deployment",
        "4.) Git branching"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "31",
      "QuestionText": "Which of the following are key principles of CD (Continuous Deployment)? (Select all that apply.)",
      "Options": [
        "1.) Automated deployments to production",
        "2.) Frequent production releases",
        "3.) Manual code reviews",
        "4.) Delayed deployments"
      ],
      "CorrectAnswer": "1,2"
    },
    {
      "Question": "32",
      "QuestionText": "What is the primary role of a CI/CD \"Artifact Repository\" in the software development process?",
      "Options": [
        "1.) To track code changes",
        "2.) To store and manage software artifacts (e.g., binaries, packages)",
        "3.) To conduct automated testing",
        "4.) To review code changes"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "33",
      "QuestionText": "Which of the following are practices associated with \"Blue-Green Deployment\"? (Select all that apply.)",
      "Options": [
        "1.) Simultaneous deployment of code changes",
        "2.) Rolling back to a previous version in case of issues",
        "3.) Deploying changes to a secondary environment",
        "4.) Testing with a small subset of users"
      ],
      "CorrectAnswer": "2,3"
    },
    {
      "Question": "34",
      "QuestionText": "Which of the following are typically included in a CI/CD \"Pipeline Configuration\"? (Select all that apply.)",
      "Options": [
        "1.) Environment variables",
        "2.) Source code files",
        "3.) Deployment scripts",
        "4.) Bug tracking system"
      ],
      "CorrectAnswer": "1,3"
    },
    {
      "Question": "35",
      "QuestionText": "In an SAP development project, the team is implementing a CI/CD pipeline. During the pipeline configuration, which components are typically included in the \"Build\" stage? (Select all that apply.)",
      "Options": [
        "1.) Compiling source code",
        "2.) Running unit tests",
        "3.) Packaging artifacts",
        "4.) Deploying to production"
      ],
      "CorrectAnswer": "1,2,3"
    },
    {
      "Question": "36",
      "QuestionText": "A development team is practicing Continuous Deployment (CD) in their SAP project. Which practices are essential for safe CD in a real-world scenario? (Select all that apply.)",
      "Options": [
        "1.) Automated testing and quality gates",
        "2.) Manual deployments to production",
        "3.) Delayed code integration",
        "4.) No testing in production"
      ],
      "CorrectAnswer": "1"
    },
    {
      "Question": "37",
      "QuestionText": "Scenario: A development team is practicing Continuous Deployment (CD) for an SAP application. What practices can help ensure the safety and reliability of CD in this scenario?",
      "Options": [
        "1.) Frequent automated testing and quality gates",
        "2.) Manual deployments to production",
        "3.) No testing in production",
        "4.) Delayed code integration"
      ],
      "CorrectAnswer": "1"
    },
    {
      "Question": "38",
      "QuestionText": "What is the purpose of a bug tracking system in SAP development?",
      "Options": [
        "1.) Managing SAP project budgets",
        "2.) Identifying defects and tracking their resolution",
        "3.) Writing SAP user documentation",
        "4.) Conducting automated SAP testing"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "39",
      "QuestionText": "What is the purpose of a code repository in SAP development?",
      "Options": [
        "1.) Tracking SAP project budgets",
        "2.) Managing SAP project timelines",
        "3.) Storing and versioning SAP source code",
        "4.) Storing SAP landscape configuration data"
      ],
      "CorrectAnswer": "3"
    },
    {
      "Question": "40",
      "QuestionText": "Scenario: In an SAP development project, the team is considering implementing a version control system. What are the benefits of using Git in this SAP scenario?",
      "Options": [
        "1.) Centralized repository management",
        "2.) Distributed architecture for offline work",
        "3.) Integration with SAP ECC",
        "4.) Streamlined SAP project budget tracking"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "41",
      "QuestionText": "You are working on an SAP BTP application that requires different levels of access based on user roles. You need to implement role-based authorization to ensure that only authorized users can perform certain actions.How can you implement role-based authorization in your SAP BTP application? (Select all that apply.)",
      "Options": [
        "1.) Configure the approuter to validate user roles during authentication",
        "2.) Include role information in security tokens issued by the IdP.",
        "3.) Implement authorization logic in the frontend user interface",
        "4.) Define and enforce role-based authorization rules in backend services."
      ],
      "CorrectAnswer": "2,4"
    },
    {
      "Question": "42",
      "QuestionText": "In CAP, what is the role of the 'srv' folder in a project?",
      "Options": [
        "1.) It contains service definitions",
        "2.) It's used for UI development",
        "3.) It stores project documentation",
        "4.) It defines the application's logic"
      ],
      "CorrectAnswer": "1"
    },
    {
      "Question": "43",
      "QuestionText": "Scenario: You want to create a Fiori application using CAP. What is the role of the 'app' folder in your project?",
      "Options": [
        "1.) It defines database tables",
        "2.) It contains UI-related files.",
        "3.) It stores business logic",
        "4.) It is not related to Fiori applications"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "44",
      "QuestionText": "Scenario: You want to restrict access to certain data in your CAP application based on user roles. What CAP feature can you use for this purpose?",
      "Options": [
        "1.) CAP authorization",
        "2.) CDS views",
        "3.) Middleware services",
        "4.) CAP security policies"
      ],
      "CorrectAnswer": "1"
    },
    {
      "Question": "45",
      "QuestionText": "Scenario: You want to create a CAP project that exposes both OData and GraphQL services. Which CAP feature can you use for this purpose? (Select all that apply.)",
      "Options": [
        "1.) OData adapter",
        "2.) GraphQL module",
        "3.) Service definitions",
        "4.) CDS views"
      ],
      "CorrectAnswer": "1,2"
    },
    {
      "Question": "46",
      "QuestionText": "What is the role of the 'schema.cds' file in a CAP project?",
      "Options": [
        "1.) It defines database schemas",
        "2.) It contains UI templates",
        "3.) It specifies deployment configurations",
        "4.) It defines CAP security policies"
      ],
      "CorrectAnswer": "1"
    },
    {
      "Question": "47",
      "QuestionText": "Scenario: You want to create a CAP project with a mobile application front end. Which technology can be used to build the mobile app in this scenario? (Select all that apply.)",
      "Options": [
        "1.) Android",
        "2.) iOS",
        "3.) SAP Fiori Mobile",
        "4.) React Native"
      ],
      "CorrectAnswer": "3,4"
    },
    {
      "Question": "48",
      "QuestionText": "Scenario: A company is planning to adopt Agile methodologies for its SAP development projects. What advantages can they expect in terms of SAP project timelines and customer satisfaction in this Agile adoption scenario? (Select all that apply.)",
      "Options": [
        "1.) Strict adherence to SAP project timelines",
        "2.) Improved collaboration and flexibility",
        "3.) Heavy SAP documentation",
        "4.) Longer development cycles"
      ],
      "CorrectAnswer": "2,4"
    },
    {
      "Question": "49",
      "QuestionText": "Scenario: You want to expose a RESTful API using CAP. Which CAP artifact is used for this purpose?",
      "Options": [
        "1.) CDS view",
        "2.) Service module",
        "3.) Data model",
        "4.) UI component"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "50",
      "QuestionText": "Scenario: You want to restrict access to certain data in your CAP application based on user roles. Which CAP feature allows you to implement this? (Select all that apply.)",
      "Options": [
        "1.) CAP authorization",
        "2.) CDS views with row-level security",
        "3.) Service events",
        "4.) UI components"
      ],
      "CorrectAnswer": "1,2"
    },
    {
      "Question": "51",
      "QuestionText": "Scenario: You have developed a CAP application, and you want to deploy it to both an on-premises environment and a cloud platform. What should you consider for successful deployment?",
      "Options": [
        "1.) Adhering to cloud-only deployment",
        "2.) Using service modules exclusively",
        "3.) Making use of CAP security policies",
        "4.) Ensuring compatibility with both environments"
      ],
      "CorrectAnswer": "4"
    },
    {
      "Question": "52",
      "QuestionText": "Scenario: Your CAP application deals with a large amount of textual data, and you want to implement full-text search capabilities. What CAP features can be used to enable full-text search? (Select all that apply.)",
      "Options": [
        "1.) Full-text search module",
        "2.) Text analytics service",
        "3.) CAP security policies",
        "4.) Service events"
      ],
      "CorrectAnswer": "1,2"
    },
    {
      "Question": "53",
      "QuestionText": "Scenario: Your CAP application needs to react to real-time events, such as order updates or notifications. What CAP feature can be used to handle real-time events?",
      "Options": [
        "1.) CDS views with calculated fields",
        "2.) Service events",
        "3.) CAP authorization",
        "4.) External services"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "54",
      "QuestionText": "Scenario: In your CAP project, you need to create calculated fields based on existing data. What CAP feature should you use for this purpose?",
      "Options": [
        "1.) Service modules",
        "2.) CDS views with calculated fields",
        "3.) UI components",
        "4.) Middleware services"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "55",
      "QuestionText": "Which of the following are benefits of Continuous Integration (CI)? (Select all that apply.)",
      "Options": [
        "1.) Reduced integration issues",
        "2.) Faster development cycles",
        "3.) Improved code quality",
        "4.) Automated deployments"
      ],
      "CorrectAnswer": "1,2,3"
    },
    {
      "Question": "56",
      "QuestionText": "Scenario: An SAP development team is considering adopting a coding standard. How does a coding standard benefit code readability in this SAP context?",
      "Options": [
        "1.) By increasing code complexity",
        "2.) By defining consistent naming conventions and formatting",
        "3.) By eliminating code reviews",
        "4.) By automating SAP landscape management"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "57",
      "QuestionText": "Scenario: A company is looking to streamline SAP deployment processes and enhance scalability. How can containerization tools like Docker contribute to these goals in this SAP deployment scenario?",
      "Options": [
        "1.) By increasing SAP project budgets",
        "2.) By simplifying SAP landscape management",
        "3.) By adding complexity to SAP deployment",
        "4.) By reducing SAP documentation efforts"
      ],
      "CorrectAnswer": "2"
    },
    {
      "Question": "58",
      "QuestionText": "Scenario: An SAP development team is adopting version control. Which version control systems are suitable for SAP development in this scenario?&nbsp; (Select all that apply.)",
      "Options": [
        "1.) Git",
        "2.) Subversion",
        "3.) Mercurial",
        "4.) Docker"
      ],
      "CorrectAnswer": "1,2"
    },
    {
      "Question": "59",
      "QuestionText": "Scenario: A company is implementing a bug tracking system for its SAP projects. How does this system aid in issue resolution and defect tracking in this SAP bug tracking scenario? (Select all that apply.)",
      "Options": [
        "1.) By increasing defects in the code",
        "2.) By automating code reviews",
        "3.) By identifying defects and tracking their resolution",
        "4.) By reducing SAP project budgets"
      ],
      "CorrectAnswer": "2,3"
    },
    {
      "Question": "60",
      "QuestionText": "Scenario: A company is implementing a bug tracking system for its SAP projects. How does this system aid in issue resolution in this SAP bug tracking scenario? (Select all that apply.)",
      "Options": [
        "1.) It introduces more defects in the code",
        "2.) It automates code reviews",
        "3.) It identifies defects and tracks their resolution",
        "4.) It eliminates the need for automated testing"
      ],
      "CorrectAnswer": "3"
    }
  ]
}

transformed_data = transform_questions(original_data)

with open("transformed_questions.json", "w", encoding="utf-8") as f:
    json.dump(transformed_data, f, indent=4, ensure_ascii=False)

print("Arquivo 'transformed_questions.json' gerado com sucesso!")

