class LikesController < ApplicationController
  def index
    @likes = Like.order('created_at DESC');
  end
end
