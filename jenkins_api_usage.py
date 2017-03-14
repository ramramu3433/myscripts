#print (dir(Jenkins))

def server_instance():
    serverurl="http://197.97.234.94"
    server = Jenkins(serverurl, username='admin', password='password')
    return server

def get_job_details():
# Refer Example #1 for definition of function 'get_server_instance'
    server = server_instance()
#    print (server.get_jobs().get_last_good_build())
 #   print (dir(server.get_jobs_info()))
    print server.get_queue()
    print server.get_latest_complete_build()
    for job_name, job_instance in server.get_jobs():
        try:

            print 'Job Name:%s' % (job_instance.name)
            print 'timestamp %s' % (job_instance.get_timestamp())
            print "last good Build %s " % (job_instance.get_last_good_build())
            print 'last build %s' % (job_instance.get_latest_build())
            print 'Job Description:%s' % (job_instance.get_description())
            print 'Is Job running:%s' % (job_instance.is_running())
            print 'Is Job enabled:%s' % (job_instance.is_enabled())
        except:
           continue
if __name__ == '__main__':
       get_job_details()

