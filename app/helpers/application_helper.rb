module ApplicationHelper

  require 'uri'
  require 'net/http'
  require 'json'

  def get_data_json(url)
    url = URI.parse(url)
    if url.kind_of?(URI::HTTP) or url.kind_of?(URI::HTTPS)
      result = Net::HTTP.get_response(url)
      result = JSON.parse(result.body)

      if !result.nil? && !result['items'].nil?
        result['items'].each do |item|
          Feed.create(date_feed: item['fecha'], title: item['title'], image: item['image'], content: item['content'], all_content: item['all_content'],
          category: item['link'])
        end
      else
        return false
      end
    end
  end
end
