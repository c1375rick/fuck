class MetasploitModule < Msf::Auxiliary
  include Msf::Exploit::Remote::HttpClient
  include Msf::Auxiliary::Scanner
  include Msf::Auxiliary::Report
  def initialize(info = {})
    super(update_info(info,
      'Name'        => 'qq scanner mobile'
      'Description' => %q{Using QQ to query mobile phone number
      },
      'References'  =>
        [
          ['URL', 'http://en.wikipedia.org/wiki/Open_proxy'],
          ['URL', 'http://nmap.org/svn/scripts/http-open-proxy.nse'],
        ],
        'Author'      => 'c-137.5 rick <1776825318[at]qq.com>',
      'License'     => MSF_LICENSE
    ))
  end
 def scanner(qq)

   qq = datastore['qq']
   url = ['']
   last_url = [url + qq]

