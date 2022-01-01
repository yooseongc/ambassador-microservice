
# Python Microservice Study: 

 * ambassador-microservice
   * microservices for ambassador
     * 3 clients: ambassador, admin, checkout
     * 5 microservices: user, email, ambassador, admin, checkout
       * user: internal web service handling 'user' (admin, ambassador are both user)
       * email: internal email service
   * admin: external web service for admin (manage products)
   * ambassador: external web service for ambassador (choose product, make order)
   * checkout: external web service for someone to checkout order (group of products suggested by an ambassador), pay for it 

 * goal
   * change architecture of service from monolith(https://github.com/antoniopapa/django-ambassador) to microservices
   * deploy microservices to Google Kubernetes Engine(GKE) with Confluent-Cloud-Kafka
   * use Stripe, Mailtrap, 

 * References
   * https://www.udemy.com/course/python-microservices/
   * https://www.djangoproject.com/
   * https://www.django-rest-framework.org/
   * https://cloud.google.com/gcp
   * https://www.confluent.io/confluent-cloud
   * https://djecrety.ir/
 
 * Tech Stack
   * Django RestFramework (for microservices)
   * MySQL8 (database)
   * Redis (for Caching)
   * Stripe (for payment handling)
   * Confluent Cloud Kafka (message-queue for synchronizing DB)
   * Mailhog (testing mail on local environment)
   * Mailtrap (testing mail on cloud environment)
   * SPA (React.js, Next.js)
   * Docker-compose (develop environment)
   * GCP K8S (deploying)
