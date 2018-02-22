class FeedsController < ApplicationController

  include ApplicationHelper

  def index
    @feeds = Feed.order('id')
  end

  def create
    get_data_json(params[:feed][:url])
    redirect_to root_path
  end

end
